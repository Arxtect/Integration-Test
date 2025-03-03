import subprocess
import os

def compile_latex(engine, tex_file, output_dir='./Results'):
    
    # 确定输出 PDF 文件名
    pdf_file = os.path.splitext(os.path.basename(tex_file))[0] + '_local.pdf'
    output_dir = os.path.join(output_dir, os.path.splitext(os.path.basename(tex_file))[0])
    pdf_path = os.path.join(output_dir, pdf_file)
    tex_file = os.path.join(tex_file, 'main.tex')
    
    # 如果输出目录不存在，则创建它
    if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} not found.")
        return

    # 调用本地 LaTeX 引擎编译 LaTeX 文件
    try:
        subprocess.run([engine, '-output-directory', output_dir, tex_file], check=True)
        generated_pdf = os.path.join(output_dir, 'main.pdf')
        if os.path.exists(generated_pdf):
            os.rename(generated_pdf, pdf_path)
        print(f"PDF compiled successfully and saved to {pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compile PDF. Error: {e}")

# 调用函数编译 LaTeX 文件到 PDF
compile_latex("xelatex", './tem-unzipped-files/test2')