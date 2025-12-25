# Subject Inference for Japanese (WIP)
A research project to reduce AI misinterpretation caused by Japanese subject omission.
日本語の主語省略による誤読を減らすための研究プロジェクトです。


## English
This project aims to reduce AI misinterpretation caused by subject omission in Japanese.
It provides logic-based rules to help language models infer omitted subjects more accurately.

## 🇯🇵 日本語
このプロジェクトは、日本語の「主語が省略されやすい問題」による  
AI の誤読をシンプルなロジックで減らすことを目指しています。

### 📄 Documentation
- [Stage 1 — Design (English)](docs/en/stage1_design.md)
- Stage 2–5: Coming soon

### 📄 ドキュメント
- [第1段階 改善案 (日本語)](docs/jp/stage1_design.md)
- 第2〜5段階：近日公開

## Languages / 言語
  - 🇯🇵 [日本語版]
  - 🇺🇸 [English version]

## Improvement Stages
- Stage 1: Speaker Identification (First-Person Omission)
- Stage 2: Clarification-Based Misinterpretation Prevention
Stage 2 prevents misinterpretation by deferring inference and requesting clarification.
- Stage 3: Contextual and Causal Inference

  - [Japanese](docs/jp/stage2_design.md)
  - [English](docs/en/stage2_design.md)

## Roadmap
- Step 1: 誤読解消の基本モデル（実装中）
- Step 2: 文脈推定の高度化（予定）
- Step 3: 多言語対応（予定）
- Step 4: IME統合モデル（予定）
- Step 5: セーフティ強化（予定）

※ このプロジェクトは継続的に更新されます。

# Mermaid
```mermaid
graph LR
    A[対話AIの誤読防止エンジン] --> B[多言語文脈モデル]
    B --> C[IME 統合]
    C --> D[誹謗中傷・詐欺検知モジュール]
    D --> E[日常AIツール群へ発展]
