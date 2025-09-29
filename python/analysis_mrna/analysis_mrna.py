from codon_table import codon_list

# 終了コドン
stop_codons = {"UAA", "UAG", "UGA"}


def find_orfs(mrna: str):
    # DNAの場合TをUに変換
    mrna = mrna.upper().replace("T", "U")

    # 返却用リスト
    orfs = []

    # mRNAの文字列分繰り返し
    for start_index in range(len(mrna)):
        # 開始文字列含む3桁が開始（AUG）の場合
        if mrna[start_index:start_index + 3] == "AUG":
            # 一時配列
            codons = []

            # 開始文字列から終端まで3桁ずつ繰り返し
            for i in range(start_index, len(mrna), 3):
                # 開始文字列含む3桁を取得
                codon = mrna[i:i + 3]

                # コドンが3桁未満の場合は終了
                if len(codon) < 3:
                    break

                # コドン表からコドン情報を取得
                aa_info = codon_list.get(codon, ("???", "不明"))
                # 一時配列にコドン情報を格納
                codons.append((codon, aa_info))

                # コドンが終了の場合
                if codon in stop_codons:
                    # 返却用配列に一時配列の値を格納
                    orfs.append(codons)
                    break
    return orfs


if __name__ == '__main__':
    test_sequences = {
        "正常なORF":
            "CCCAUGUUUCUUAUCGUAAGCCCCACGGCGCAUCAGAACAAAGAUGAGUGUUAAAAA",
        "正常なORF（複数）":
            "AUGUCGUCUCUGUAAAUGUUCCAAGCGUAA",
        "正常なDNA":
            "ATGTTGCGTGGATAA",
        "未知の塩基": "AUGUGGCGAAXGGGCUAA",  # AXG → "??? 不明"
        "不完全コドン": "AUGUUUCGG",  # 終了なし"
        "開始なし": "CCCUUUUGA",  # AUGがないので翻訳開始しない
    }

    # テストシーケンス分繰り返し
    for label, seq in test_sequences.items():
        # テストケース名表示
        print(f"--- {label} ---")

        # mRNA/DNA解析
        orfs = find_orfs(seq)

        # 解析結果判定
        if not orfs:
            print("  ORFなし")
        else:
            # 解析結果分繰り返し（indexは1スタート）
            for idx, orf in enumerate(orfs, 1):
                print(f"  ORF {idx}:")
                # 解析結果のコドン分繰り返し[コドン,(英名, 和名)]
                for codon, (abbr, jp) in orf:
                    print(f"    {codon} -> {abbr}: {jp}")
