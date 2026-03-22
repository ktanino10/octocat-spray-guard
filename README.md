# 🎨 Octocat Spray Guard (Stencil)

> 🇯🇵 **日本語版はこちら → [下へスクロール](#-octocat-スプレーガードステンシル)**

## Overview

A 3D-printable **spray paint stencil (guard)** of the GitHub Octocat logo. Place it on a paper bag or other surface, spray paint through the cutout, and transfer the Octocat logo cleanly.

**Two versions are included:**

- **Normal version** — Octocat silhouette is cut out (white cutout). Spray through it to paint the Octocat shape.
- **Inverse version** — Background around Octocat is cut out (black cutout). Spray through it to paint everything *except* the Octocat, leaving it as a white silhouette.

This project was created as a **personal experiment** using [GitHub Copilot CLI](https://docs.github.com/en/copilot) to auto-generate 3D CAD files from a logo image.

![GitHub Mark](GitHub-Mark-ea2971cee799.png)

## Model Specs

| Parameter | Value |
|---|---|
| Shape | Square stencil with Octocat cutout |
| Overall size | 100 mm × 100 mm |
| Logo area | 60 mm × 60 mm (center) |
| Guard margin | 20 mm per side |
| Thickness | 3 mm |
| Mesh | Watertight (3D-print ready) |
| Versions | Normal (white cutout) + Inverse (black cutout) |

## Files

| File | Format | Description |
|---|---|---|
| `octocat_spray_guard.stl` | STL | Normal version — Octocat silhouette cutout (Git LFS) |
| `octocat_spray_guard.obj` | OBJ | Normal version — OBJ format (Git LFS) |
| `octocat_spray_guard.3mf` | 3MF | Normal version — 3MF format |
| `octocat_spray_guard_inverse.stl` | STL | Inverse version — background cutout (Git LFS) |
| `octocat_spray_guard_inverse.obj` | OBJ | Inverse version — OBJ format (Git LFS) |
| `octocat_spray_guard_inverse.3mf` | 3MF | Inverse version — 3MF format |
| `generate_spray_guard.py` | Python | Generation script (generates both versions) |
| `GitHub-Mark-ea2971cee799.png` | PNG | Source image |

## How to Use

1. **3D print** the stencil (PLA recommended, 100% infill)
2. **Place** the stencil on a paper bag or target surface
3. **Spray paint** through the cutout
4. **Remove** the stencil →
   - **Normal version**: Octocat logo is painted on the surface
   - **Inverse version**: Octocat remains unpainted (white silhouette) with painted surroundings

## Recommended Print Settings

```
Layer height:  0.2 mm
Infill:        100%
Support:       Not needed
Material:      PLA recommended
Nozzle temp:   200–210 °C
Bed temp:      60 °C
```

## Customization

Edit the parameters at the top of `generate_spray_guard.py`:

```python
EXTRUDE_HEIGHT = 3.0    # Stencil thickness (mm)
LOGO_AREA_SIZE = 60.0   # Logo area size (mm)
GUARD_MARGIN   = 20.0   # Guard width around logo (mm)
```

Then run:

```bash
pip install Pillow numpy numpy-stl scipy trimesh
python generate_spray_guard.py
```

## ⚠️ Disclaimer / Non-Commercial Use

- This project is for **personal and educational purposes only**. It is **not intended for commercial use**.
- The GitHub logo and Octocat are **trademarks of GitHub, Inc.** This project is not affiliated with, endorsed by, or sponsored by GitHub.
- Please refer to the [GitHub Logo Usage Guidelines](https://github.com/logos) before using or distributing any output.

## Making-of Video

[![Making-of Video](https://img.youtube.com/vi/PxDf4HDmUJs/0.jpg)](https://youtu.be/PxDf4HDmUJs)

▶️ [Watch the making-of on YouTube](https://youtu.be/PxDf4HDmUJs)

## Related

- [copilot-cli-cad-experiment](https://github.com/ktanino10/copilot-cli-cad-experiment) — Original CAD generation experiment

---

# 🎨 Octocat スプレーガード（ステンシル）

## 概要

GitHub Octocatロゴの**スプレー塗装用ガード（ステンシル）**の3Dプリントモデルです。紙袋などの上に置いてスプレーすると、くり抜き部分を通してOctocatロゴをきれいに転写できます。

**2種類のバージョンを同梱：**

- **通常版** — Octocatシルエット（白い部分）をくり抜き。スプレーするとOctocatの形が転写される。
- **反転版** — Octocat周囲の背景（黒い部分）をくり抜き。スプレーするとOctocatの周りが塗られ、Octocatが白抜きになる。

このプロジェクトは [GitHub Copilot CLI](https://docs.github.com/ja/copilot) を使って、ロゴ画像から3D CADファイルを自動生成する**個人的な実験**として作成しました。

## モデル仕様

| パラメータ | 値 |
|---|---|
| 形状 | 正方形ステンシル（Octocatくり抜き） |
| 全体サイズ | 100 mm × 100 mm |
| ロゴ部分 | 60 mm × 60 mm（中央） |
| ガード幅 | 各辺 20 mm |
| 厚み | 3 mm |
| メッシュ | 水密（3Dプリント対応） |
| バージョン | 通常版（白くり抜き）＋ 反転版（黒くり抜き） |

## ファイル一覧

| ファイル | 形式 | 説明 |
|---|---|---|
| `octocat_spray_guard.stl` | STL | 通常版 — Octocatシルエットくり抜き (Git LFS) |
| `octocat_spray_guard.obj` | OBJ | 通常版 — OBJ形式 (Git LFS) |
| `octocat_spray_guard.3mf` | 3MF | 通常版 — 3MF形式 |
| `octocat_spray_guard_inverse.stl` | STL | 反転版 — 背景くり抜き (Git LFS) |
| `octocat_spray_guard_inverse.obj` | OBJ | 反転版 — OBJ形式 (Git LFS) |
| `octocat_spray_guard_inverse.3mf` | 3MF | 反転版 — 3MF形式 |
| `generate_spray_guard.py` | Python | 生成スクリプト（両バージョン生成） |
| `GitHub-Mark-ea2971cee799.png` | PNG | 入力画像 |

## 使い方

1. ステンシルを **3Dプリント** する（PLA推奨、インフィル100%）
2. 紙袋や対象面の上にステンシルを **置く**
3. くり抜き部分から **スプレー塗装** する
4. ステンシルを **外す** →
   - **通常版**: Octocatロゴが紙袋に転写される
   - **反転版**: Octocatが白抜きで残り、周囲が塗られる

## 3Dプリント推奨設定

```
レイヤー高さ:  0.2 mm
インフィル:    100%
サポート:      不要
素材:          PLA推奨
ノズル温度:    200–210 °C
ベッド温度:    60 °C
```

## カスタマイズ

`generate_spray_guard.py` 冒頭のパラメータを変更してください：

```python
EXTRUDE_HEIGHT = 3.0    # ステンシルの厚み (mm)
LOGO_AREA_SIZE = 60.0   # ロゴ部分のサイズ (mm)
GUARD_MARGIN   = 20.0   # ロゴ周囲のガード幅 (mm)
```

実行：

```bash
pip install Pillow numpy numpy-stl scipy trimesh
python generate_spray_guard.py
```

## ⚠️ 免責事項・非商用利用について

- 本プロジェクトは**個人的・教育目的のみ**で作成されています。**商用利用は一切意図していません。**
- GitHubロゴおよびOctocatは **GitHub, Inc. の商標** です。本プロジェクトはGitHubとの提携・推奨・後援を受けたものではありません。
- 出力物の使用・配布にあたっては、[GitHubロゴ使用ガイドライン](https://github.com/logos)をご確認ください。

## 制作記録

[![制作記録](https://img.youtube.com/vi/PxDf4HDmUJs/0.jpg)](https://youtu.be/PxDf4HDmUJs)

▶️ [YouTubeで制作記録を見る](https://youtu.be/PxDf4HDmUJs)

## 関連プロジェクト

- [copilot-cli-cad-experiment](https://github.com/ktanino10/copilot-cli-cad-experiment) — 元のCAD生成実験リポジトリ
