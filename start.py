import os

def scan_markdown_files():
    # 获取当前文件夹路径
    current_directory = os.getcwd()
    
    # 列出当前文件夹内的所有文件
    files = os.listdir(current_directory)
    
    # 存放 Markdown 文件的列表
    markdown_files = []
    
    # 遍历文件，筛选出 Markdown 文件
    for file in files:
        if file.endswith('.md') and file.lower() != 'readme.md':
            markdown_files.append(file)
    
    # 输出 Markdown 文件的格式，用逗号隔开
    output = ', '.join(f"[{md_file[:-3]}](./{md_file[:-3]})" for md_file in markdown_files)
    print(output)

if __name__ == "__main__":
    scan_markdown_files()
