import time
import asyncio
import requests

async def funct1():
    url = "https://cdn.wallpapersafari.com/21/34/C36PkS.jpg"
    response =requests.get(url)
    open("image1.jpg","wb").write(response.content)
    print("funct1")
    return "Prabhakar"

async def funct2():
    url = "https://images.wallpapersden.com/image/city-landscape-4k-top-view_bmZqbGaUmZqaraWkpJRobmVprWdnaWU.jpg"
    response =requests.get(url)
    open("image2.jpg","wb").write(response.content)
    print("funct2")

async def funct3():
    url = " https://i.pinimg.com/564x/8b/4c/7e/8b4c7e12b25ae6cb5668b8dfbd486191.jpg"
    response =requests.get(url)
    open("image3.jpg","wb").write(response.content)
    print("funct3")


async def main():
    # task = asyncio.create_task(funct1())
    # await funct1()
    # await funct2()
    # await funct3()

    l= await asyncio.gather(
        funct1(),
        funct2(),
        funct3(),
    )
    print(l)

asyncio.run(main())