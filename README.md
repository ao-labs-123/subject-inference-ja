日本語の主語省略による誤読を減らすための研究プロジェクトです。

## 🇯🇵 日本語
このプロジェクトは、日本語の「主語が省略されやすい問題」による  
AI の誤読をシンプルなロジックで減らすことを目指しています。

### 📄 ドキュメント
- [第1段階 改善案 (日本語)](docs/jp/stage1_design.md)
- 第2〜5段階：近日公開

  - [Japanese](docs/jp/stage2_design.md)
  - [English](docs/en/stage2_design.md)

# Subject Inference – Stage 2

## Overview (EN)
This repository presents a clarification-based mechanism designed to
prevent premature commitment to incorrect interpretations in dialogue AI.
Stage 2 focuses on ambiguity detection and minimal clarification,
not semantic inference.

## 概要 (JP)
本リポジトリは、対話AIにおける誤読の原因となる
「早期の意味確定」を防ぐための確認機構を提案・実装するものです。
Stage 2 では意味推論は行わず、主語不明・曖昧性に対する
最小限の聞き返しのみを行います。

## Status
- Design: Stable
- Implementation: Reference / Experimental

## License
MIT

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
