import re
import sys
import time

"""
This file is used to format the content of markdown file which is export by ipython notebook.
More function will be update later.
Author: Andrew Guan
"""


class FormatContent:

    def _remove_u(self, txt):
        return txt.replace("\u200b    ", "")

    def _remove_mat(self, txt):
        return re.sub(r"\s{4}\[<.*?>]", "", txt)

    def _remove_mul_n(self, txt):
        return re.sub(r"[\n]{2,}", r"\n\n", txt)

    def _replace_img(self, txt):
        g1 = r"(\!\[.*?\][(])"
        g2 = r"(.*?)"
        g3 = r"([)])"

        head_s = r'<center><img src="https://cdn.jsdelivr.net/gh/AllenWrong/BlogCDN/img/'
        tail_s = r'"/></center>'

        return re.sub(g1 + g2 + g3, head_s + r"\2" + tail_s, txt)

    def time_stamp_to_time(self, timestamp, more=False):
        timeStruct = time.localtime(timestamp)
        if more:
            return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
        return time.strftime('%Y-%m-%d', timeStruct)

    def run(self, input_file):
        """
        Args:
            input_file: must be the file in the current directory
        """
        with open(input_file, "r", encoding="utf-8") as f:
            txt = f.read()

        txt = self._remove_u(txt)
        txt = self._remove_mat(txt)
        txt = self._remove_mul_n(txt)
        txt = self._replace_img(txt)

        header = f'---\n' \
                 f'layout: post\n' \
                 f'omments: true\n' \
                 f'title: "{input_file.split(".")[0]}"\n' \
                 f'excerpt: ""\n' \
                 f'date: {self.time_stamp_to_time(time.time(), True)}\n' \
                 f'mathjax: false\n' \
                 f"---\n"
        txt = header + txt

        with open("./" + "f_" + input_file, "w") as f:
            f.write(txt)


if __name__ == '__main__':
    format_eng = FormatContent()
    format_eng.run(sys.argv[1])
