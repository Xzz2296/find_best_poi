import fileinput

start_line = 79
end_line = 32102

# 打开文件并修复每一行
with fileinput.FileInput('E:\\xpj\\research\\POI\\psqlcsv\\kolkata_img_location.sql', inplace=True, backup='.bak') as f:
    for i, line in enumerate(f, start=1):
        # 如果行号在指定范围内
        if start_line <= i <= end_line:
            # 如果行的末尾是'\N'，跳过
            if line.strip().endswith('\\N'):
                print(line, end='')
            # 如果行的末尾缺少引号，添加一个引号
            elif not line.strip().endswith('"'):
                print(line.strip() + '"', end='\n')
            else:
                print(line, end='')
        else:
            print(line, end='')