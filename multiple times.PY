########### cmd ###########
D:/Software/Tool/Psychopy/python.exe -m pip install replicate

########### py ###########
import replicate
import os

# set API token
os.environ["REPLICATE_API_TOKEN"] = "x"

########### single file ten times ###########
# FOR loop
for i in range(10):
    print(f"\n=== 第 {i+1} 次运行 ===，s1-1.b-low high")
    
    # input
    input = {
        "input_audio": open(r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-1.b-low high.wav", "rb")
    }

    # run
    output = replicate.run(
        "ictnlp/llama-omni:36c9bcf70a56f40d9a27445c30c769308b18180296749f86ec9b682baf7ad351",
        input=input
    )
    print(output)

########### multiple files ten times ###########
# file list
files = [
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-1.b-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-1.c-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-2.a-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-2.b-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-2.c-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-3.a-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-3.b-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-3.c-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-4.a-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-4.b-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-4.c-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-5.a-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-5.b-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-5.c-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-6.a-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-6.b-low high.wav",
    r"D:\Download\MLLM\pilot 3_item\set 1_1-6_mllm\low high\s1-6.c-low high.wav"
]

# FOR loop
for file_path in files:
    print(f"\n=== 开始处理文件: {os.path.basename(file_path)} ===")
    
    for i in range(10):
        print(f"\n--- 第 {i+1} 次运行 ---")
        
        # input
        input = {
            "input_audio": open(file_path, "rb")
        }

        # model
        output = replicate.run(
            "ictnlp/llama-omni:36c9bcf70a56f40d9a27445c30c769308b18180296749f86ec9b682baf7ad351",
            input=input
        )
        print(output)
