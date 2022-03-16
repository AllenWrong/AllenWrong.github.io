import pandas as pd
import sys


def csv_to_mdtable(csv_file, out_file):
    df = pd.read_csv("./multi-modal-papers.csv", header=None)
    header = "| 会议/期刊 | 论文 |\n| ---- | ---- |\n"
    content = ""
    for i in range(df.shape[0]):
        content += "| " + " | ".join(df.iloc[i, :].tolist()) + " |\n"
    with open("./Papers.md", "w", encoding="utf-8") as f:
        f.write(header + content)
        
        
if __name__ == '__main__':
    csv_to_mdtable(sys.argv[1], sys.argv[2])