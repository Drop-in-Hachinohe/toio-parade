import aioconsole
import asyncio
from toio import *

toio_33n = [50, 50]

# 1秒かけて前に進む
async def go_forward(cube, ms):
    await cube.api.motor.motor_control(toio_33n[0], toio_33n[1], ms)

# 1秒かけて後ろに進む
async def go_back(cube, ms):
    await cube.api.motor.motor_control(toio_33n[0] * -1, toio_33n[1] *  -1, ms)

# 1秒かけて反時計回り
async def turn_left(cube):
    await cube.api.motor.motor_control(toio_33n[0] * -1, toio_33n[1], 1000)
    await asyncio.sleep(1)

# 1秒かけて時計回り
async def turn_right(cube):
    await cube.api.motor.motor_control(toio_33n[0], toio_33n[1] * -1, 1000)
    await asyncio.sleep(1)

# 反時計回りに旋回
async def curve_forward_left(cube, ms):
    await cube.api.motor.motor_control(30, 50, ms)

# 時計回りに旋回
async def curve_forward_right(cube, ms):
    await cube.api.motor.motor_control(50, 30, ms)

# 行ったり来たり
async def go_fb(cube):
    await go_forward(cube, 1000)
    await asyncio.sleep(1.25)
    await go_back(cube, 1000)
    await asyncio.sleep(1.25)

# 行ったり来たり (reverse)
async def go_fb_r(cube):
    await go_back(cube, 1000)
    await asyncio.sleep(1.25)
    await go_forward(cube, 1000)
    await asyncio.sleep(1.25)

async def w1(cube, is_reprise=False):
    # 行ったり来たり
    await go_fb(cube)

    # 時計回り
    await turn_right(cube)

    # 反時計回り
    await turn_left(cube)
    await asyncio.sleep(0.5)

    for i in range(4):
        for j in range(3):
            if j != 2:
                await go_forward(cube, 800)
                await asyncio.sleep(1.05)
            else:
                await go_forward(cube, 500)
        await asyncio.sleep(0.75)

        if i != 3 or not is_reprise:
            await go_forward(cube, 500)
            await asyncio.sleep(0.75)

            # 時計回り
            await turn_right(cube)
            await asyncio.sleep(0.25)

        elif i == 3 and is_reprise:
            for k in range(5):
                # 時計回り
                await turn_right(cube)


async def w2(cube):
    # 左に旋回
    await curve_forward_left(cube, 1250 * 2)
    await asyncio.sleep(2.75)

    # 右に旋回
    await curve_forward_right(cube, 1250 * 2)
    await asyncio.sleep(2.75)

    # 右に旋回
    await curve_forward_right(cube, 1500)
    await asyncio.sleep(1.65)

    # 左に旋回
    await curve_forward_left(cube, 1500)
    await asyncio.sleep(1.5)

    # 時計回り
    await turn_right(cube)

    # 反時計回り
    await turn_left(cube)
    await asyncio.sleep(0.5)

    for j in range(3):
        if j != 2:
            await go_forward(cube, 800)
            await asyncio.sleep(1.1)
        else:
            await go_forward(cube, 500)
    await asyncio.sleep(0.75)

    await go_forward(cube, 500)
    await asyncio.sleep(0.75)

    # 時計回り
    await turn_right(cube)
    await asyncio.sleep(1.25)

async def w3(cube):
    for i in range(4):
        for j in range(3):
            if j != 2:
                await go_forward(cube, 800)
                await asyncio.sleep(1.05)
            else:
                await go_forward(cube, 500)
        await asyncio.sleep(0.75)

        await go_forward(cube, 500)
        await asyncio.sleep(0.75)

        # 時計回り
        await turn_right(cube)
        await asyncio.sleep(0.25)

async def w4(cube):
    for i in range(2):
        # 時計回り
        await turn_right(cube)

        # 反時計回り
        await turn_left(cube)

    # 時計回り 
    await turn_right(cube)

    for l in range(2):

        for i in range(3):
            for j in range(3):
                if j != 2:
                    await go_forward(cube, 750)
                    await asyncio.sleep(1)
                else:
                    await go_forward(cube, 500)
            await asyncio.sleep(0.75)

            await go_forward(cube, 500)
            await asyncio.sleep(0.75)

            # 時計回り
            await turn_right(cube)
            await asyncio.sleep(0.25)

        for i in range(4):
            # 反時計回り
            await turn_left(cube)

async def w5(cube):
    # 右に旋回
    await curve_forward_right(cube, 1500)
    await asyncio.sleep(1.5)

    # 左に旋回
    await curve_forward_left(cube, 1500)
    await asyncio.sleep(1.65)

    # 時計回り
    await turn_right(cube)

    # 右に旋回
    await curve_forward_right(cube, 1500)
    await asyncio.sleep(1.5)

    # 左に旋回
    await curve_forward_left(cube, 1500)
    await asyncio.sleep(1.65)

    # 反時計回り
    for i in range(2):
        await turn_left(cube)

    # 時計回り
    for i in range(2):
        await turn_right(cube)

async def w6(cube):
    for i in range(3):
        for j in range(3):
            if j != 2:
                await go_forward(cube, 800)
                await asyncio.sleep(1.05)
            else:
                await go_forward(cube, 500)
        await asyncio.sleep(0.75)

        await go_forward(cube, 500)
        await asyncio.sleep(0.75)

        # 時計回り
        await turn_right(cube)
        await asyncio.sleep(0.25)

    # 右に旋回
    await curve_forward_right(cube, 1500)
    await asyncio.sleep(1.5)

    # 左に旋回
    await curve_forward_left(cube, 1500)
    await asyncio.sleep(1.65)


# わちゃわちゃ (個体差あるし) パレードおもちゃの兵隊の行進
async def wachax2_parade(cube):
    # wachawach_No.1
    await w1(cube)

    # wachawach_No.2
    await w2(cube)

    # wachawach_No.3
    await w3(cube)

    # wachawach_No.4
    await w4(cube)

    # wachawach_No.5
    await w5(cube)

    # wachawach_No.6
    await w6(cube)

    # wachawach_No.7
    await w1(cube, True)

# メイン処理
async def gogo():
    # 本番はこちらを実行
    async with MultipleToioCoreCubes(cubes=6) as cubes:
            print(f"{len(cubes)} 台接続完了！")
            print("sキーでわちゃわちゃ開始...")

            # sキー入力待ち
            while True:
                cmd = await aioconsole.ainput(">>> ")
                if cmd.lower() == "s":
                    break

            # 各キューブで並列にわちゃわちゃ開始
            await asyncio.gather(*(wachax2_parade(cube) for cube in cubes))

            # 全員停止
            await asyncio.gather(*(cube.api.motor.motor_control(0, 0) for cube in cubes))
            print("全員停止！")

    # # 1台のキューブをスキャン (テスト用)
    # dev_list = await BLEScanner.scan(1)
    # assert len(dev_list), "キューブが見つかりませんでした"
    #
    # # キューブに接続
    # cube = ToioCoreCube(dev_list[0].interface)
    # await cube.connect()
    # print("接続しました")
    #
    # # 前進（速度255で1秒間）
    # await wachax2_parade(cube)
    #
    # # 停止
    # await cube.api.motor.motor_control(0, 0)
    # print("停止しました")
    #
    # # 切断
    # await cube.disconnect()
    # print("切断しました")

# メイン実行
asyncio.run(gogo())

