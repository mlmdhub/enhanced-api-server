from aiohttp import web


async def handle(request):
    """
    处理HTTP请求的协程函数
    """
    # 获取请求中的参数等信息（示例中暂未深度使用参数）
    name = request.match_info.get('name', "Anonymous")
    text = f"Hello, {name}"
    return web.Response(text=text)


async def main():
    """
    主函数，用于创建和启动服务器
    """
    app = web.Application()
    # 添加路由，将根路径及带有名字参数的路径都映射到handle函数处理
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8080)
    await site.start()
    print("服务器已启动，正在监听 http://127.0.0.1:8080")
    # 保持服务器运行
    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
