# nolhallsym

`nolhallsym` は、磁気CIFファイル（.mcif）を入力として、Drude項、BCD項、interband QMD項、およびintraband QMD項のテンソル形状を解析・可視化するためのツールです。

本プログラムにおける磁気対称性の取り扱いは、以下の論文の理論を参考にしています。

> Y. Ulrich et al., *Phys. Rev. B* **113**, L201107 (2026).

## インストール

本ライブラリは以下のコマンドでインストール可能です。
※Gitがインストールされている環境で実行してください。

```bash
pip install git+[https://github.com/xx/nolhallsym.git](https://github.com/xx/nolhallsym.git)
```

## 使い方

インストール後、ターミナルから以下のコマンドを実行することで解析が始まります。

Bash

```
nolhallsym <対象の.mcifファイル>
```

**実行例:**

Bash

```
nolhallsym CuMnAs.mcif
```

コマンドを実行すると、現在のディレクトリに解析結果がPDF形式で生成されます（例: `mcif_tensor_CuMnAs.pdf`）。

## 出力例

解析が完了すると、各項のテンソル形状を示すPDFが出力されます。

![sample_0002](src/nolhallsym/assets/demo/mcif_tensor_CuMnAs.pdf)

## 参考文献

本ツールの実装にあたっては、以下の研究を参考にしています。

- Y. Ulrich, et al., "..." *Phys. Rev. B* **113**, L201107 (2026).
- 

## ライセンス

本プロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](https://www.google.com/search?q=LICENSE) ファイルをご確認ください。
