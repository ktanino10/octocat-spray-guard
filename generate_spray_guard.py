"""
GitHub Octocat スプレー塗装用ガード（ステンシル）生成
- 正方形の板にOctocatシルエットをくり抜いた貫通型モデル
- 紙袋等に置いてスプレーすると、くり抜き部分だけ塗料が通りロゴが転写される
- 正方形の縁を広めにとり、スプレーが外に漏れないようにする
- 通常版（白くり抜き）と反転版（黒くり抜き）の2種類を生成
"""

import numpy as np
from PIL import Image
from scipy import ndimage
from stl import mesh as stlmesh
import trimesh
import os

# === Parameters (mm) ===
EXTRUDE_HEIGHT = 3.0    # ステンシルの厚み（薄めの方が使いやすい）
RESOLUTION = 500        # グリッド解像度
LOGO_AREA_SIZE = 60.0   # ロゴ部分のサイズ (mm)
GUARD_MARGIN = 20.0     # ロゴ周囲のガード幅 (mm) — スプレーが外に出ない余裕
TOTAL_SIZE = LOGO_AREA_SIZE + GUARD_MARGIN * 2  # 正方形全体のサイズ (100mm)

# 出力先
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- 画像読み込み・処理 ---
img = Image.open(os.path.join(OUTPUT_DIR, "GitHub-Mark-ea2971cee799.png"))
img = img.convert("L")
img = img.resize((RESOLUTION, RESOLUTION), Image.LANCZOS)
pixels = np.array(img)

# 二値化: 黒(dark)=True
black_mask = pixels < 128

# スムージングでギザギザを軽減
smoothed = ndimage.gaussian_filter(black_mask.astype(float), sigma=1.5)
black_mask = smoothed > 0.5

# 円の範囲内だけ取得（外側の余白は除外）
y, x = np.ogrid[:RESOLUTION, :RESOLUTION]
center = RESOLUTION / 2
radius_px = RESOLUTION * 0.48
circle_mask = ((x - center) ** 2 + (y - center) ** 2) <= radius_px ** 2

# 通常版: 白部分（Octocatシルエット）= くり抜く部分
octocat_mask = (~black_mask) & circle_mask

# 反転版: 黒部分（Octocat周囲の背景）= くり抜く部分
inverse_mask = black_mask & circle_mask

# --- 正方形ガード用の拡大グリッド作成 ---
margin_px = int(GUARD_MARGIN / LOGO_AREA_SIZE * RESOLUTION)
total_px = RESOLUTION + margin_px * 2
scale = TOTAL_SIZE / total_px


def build_guard_mask(cutout_mask):
    """くり抜きマスクから正方形ガード全体のマスクを生成する。"""
    guard = np.ones((total_px, total_px), dtype=bool)
    guard[margin_px:margin_px + RESOLUTION, margin_px:margin_px + RESOLUTION][cutout_mask] = False
    return guard


guard_mask_normal = build_guard_mask(octocat_mask)
guard_mask_inverse = build_guard_mask(inverse_mask)

print(f"=== スプレーガード（ステンシル）生成 ===")
print(f"  全体サイズ: {TOTAL_SIZE:.0f}mm × {TOTAL_SIZE:.0f}mm (正方形)")
print(f"  ロゴ部分: {LOGO_AREA_SIZE:.0f}mm × {LOGO_AREA_SIZE:.0f}mm")
print(f"  ガード幅: {GUARD_MARGIN:.0f}mm")
print(f"  厚み: {EXTRUDE_HEIGHT:.1f}mm")
print(f"  グリッド: {total_px} × {total_px} px")
print()


def mask_to_watertight_stl(mask, scale, height, filename):
    """2Dマスクから貫通型（空洞あり）の水密STLメッシュを生成。"""
    rows, cols = mask.shape
    triangles = []

    for i in range(rows):
        for j in range(cols):
            if not mask[i, j]:
                continue

            x0 = j * scale
            y0 = i * scale
            x1 = (j + 1) * scale
            y1 = (i + 1) * scale

            # Top face (z = height)
            triangles.append([[x0, y0, height], [x1, y0, height], [x0, y1, height]])
            triangles.append([[x1, y0, height], [x1, y1, height], [x0, y1, height]])

            # Bottom face (z = 0)
            triangles.append([[x0, y0, 0], [x0, y1, 0], [x1, y0, 0]])
            triangles.append([[x1, y0, 0], [x0, y1, 0], [x1, y1, 0]])

            # Side walls — 隣が空洞 or 端の場合のみ壁を作る
            if j + 1 >= cols or not mask[i, j + 1]:
                triangles.append([[x1, y0, 0], [x1, y1, 0], [x1, y0, height]])
                triangles.append([[x1, y1, 0], [x1, y1, height], [x1, y0, height]])

            if j - 1 < 0 or not mask[i, j - 1]:
                triangles.append([[x0, y0, 0], [x0, y0, height], [x0, y1, 0]])
                triangles.append([[x0, y1, 0], [x0, y0, height], [x0, y1, height]])

            if i + 1 >= rows or not mask[i + 1, j]:
                triangles.append([[x0, y1, 0], [x0, y1, height], [x1, y1, 0]])
                triangles.append([[x1, y1, 0], [x0, y1, height], [x1, y1, height]])

            if i - 1 < 0 or not mask[i - 1, j]:
                triangles.append([[x0, y0, 0], [x1, y0, 0], [x0, y0, height]])
                triangles.append([[x1, y0, 0], [x1, y0, height], [x0, y0, height]])

    print(f"  三角形数: {len(triangles):,}")

    stl_obj = stlmesh.Mesh(np.zeros(len(triangles), dtype=stlmesh.Mesh.dtype))
    for idx, tri in enumerate(triangles):
        for v in range(3):
            stl_obj.vectors[idx][v] = tri[v]

    stl_obj.save(filename)
    size_kb = os.path.getsize(filename) / 1024
    print(f"  保存: {filename} ({size_kb:.0f} KB)")
    return filename


def generate_all_formats(guard_mask, base_name, label):
    """STL/OBJ/3MFの3形式をまとめて生成する。"""
    print(f"--- {label} ---")
    print("STL生成中...")
    stl_path = os.path.join(OUTPUT_DIR, f"{base_name}.stl")
    mask_to_watertight_stl(guard_mask, scale, EXTRUDE_HEIGHT, stl_path)

    print("フォーマット変換中...")
    tmesh = trimesh.load(stl_path)

    obj_path = os.path.join(OUTPUT_DIR, f"{base_name}.obj")
    tmesh.export(obj_path, file_type="obj")
    print(f"  OBJ: {obj_path} ({os.path.getsize(obj_path)/1024:.0f} KB)")

    threemf_path = os.path.join(OUTPUT_DIR, f"{base_name}.3mf")
    tmesh.export(threemf_path, file_type="3mf")
    print(f"  3MF: {threemf_path} ({os.path.getsize(threemf_path)/1024:.0f} KB)")
    print()


# === 通常版: 白くり抜き（Octocatシルエットが穴） ===
generate_all_formats(guard_mask_normal, "octocat_spray_guard",
                     "通常版（白くり抜き：Octocatシルエットが穴）")

# === 反転版: 黒くり抜き（Octocat周囲が穴） ===
generate_all_formats(guard_mask_inverse, "octocat_spray_guard_inverse",
                     "反転版（黒くり抜き：Octocat周囲が穴）")

print(f"✅ 両バージョン生成完了！")
print(f"\n=== モデル仕様 ===")
print(f"  形状: 正方形ステンシル（100mm × 100mm × {EXTRUDE_HEIGHT:.1f}mm）")
print(f"  ガード幅: 各辺 {GUARD_MARGIN:.0f}mm")
print(f"\n=== 通常版 (octocat_spray_guard) ===")
print(f"  白い部分（Octocatシルエット）をくり抜き")
print(f"  → スプレーするとOctocatの形が転写される")
print(f"\n=== 反転版 (octocat_spray_guard_inverse) ===")
print(f"  黒い部分（Octocat周囲の背景）をくり抜き")
print(f"  → スプレーするとOctocatの周りが塗られ、Octocatが白抜きになる")
