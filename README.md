## Languages / 言語
  - 🇯🇵 [日本語版]
  - 🇺🇸 [English version]

## Improvement Stages
- Stage 1: Speaker Identification (First-Person Omission)
- Stage 2: Clarification-Based Misinterpretation Prevention
- Stage 3: Contextual and Causal Inference

Stage 2 prevents misinterpretation by deferring inference and requesting clarification.

  - [Japanese](https://github.com/ao-labs-123/subject-inference-ja/tree/main.)
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
