# cmd
D:/Software/Tool/Psychopy/python.exe -m pip install replicate

import replicate
import os

# set API token
os.environ["REPLICATE_API_TOKEN"] = "x"

# multiple times
for i in range(10):
    print(f"\n=== 第 {i+1} 次运行 ===")
    
    # input
    input = {
        "input_audio": open(r"D:\x.wav", "rb")
    }

    # run
    output = replicate.run(
        "ictnlp/llama-omni:36c9bcf70a56f40d9a27445c30c769308b18180296749f86ec9b682baf7ad351",
        input=input
    )
    print(output)