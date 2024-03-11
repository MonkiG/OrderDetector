import asyncio


from basic_transcribe import basic_transcribe


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(basic_transcribe())
    loop.close()


if __name__ == "__main__":
    main()
