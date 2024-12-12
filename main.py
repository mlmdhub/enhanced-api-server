import sys
import json
import subprocess


def main():
    if len(sys.argv) < 2:
        print("参数传递不完整，请传入参数", file=sys.stderr)
        sys.exit(1)
    try:
        # 获取传入的参数（假设传入的是JSON字符串，这里进行解析）
        param = json.loads(sys.argv[1])
        print(f"接收到的参数: {param}")
        # 在这里可以进行后续对参数的使用、处理等操作
        result = process_param(param)
        print(f"处理结果: {result}")
    except json.JSONDecodeError as e:
        print(f"参数解析错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"其他错误: {e}", file=sys.stderr)
        sys.exit(1)


def process_param(param):
    # 这里是对传入参数进行处理的示例函数，你可以根据实际需求替换具体逻辑
    return param['key'].upper()


if __name__ == "__main__":
    main()