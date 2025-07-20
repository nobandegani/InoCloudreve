import asyncio

from src.CloudreveClient import CloudreveClient
from src.CloudreveClient.utils import save_url_as_file


async def main():
    client = CloudreveClient("https://drive.likenesslabs.com/api/v4", "spark@likenesslabs.com", "9U3strQen3tWgxC")
    ping_result = await client.ping()
    print("Ping response:", ping_result)

    password_login_result = await client.password_sign_in()
    print("password_login_result:", password_login_result)

    print("is_token_valid:",client.is_token_valid())

    #refresh_token_result = await client.refresh_token()
    #print ("refresh_token_result:",refresh_token_result)

    #example_file_path = "Spark/test"
    example_file_path = "Spark/test/input/TanaRain_073.png"

    result = await client.get_download_url(example_file_path, False)
    print("result:", result)
    print("url:", result["url"])

    save_url_as_file_result = await client.save_url_as_file(
        result["url"],
        r"E:\NIL\spark\python\InoGenie\assets\example batch",
        result["file_name"],
        result["extension"])
    print("save_url_as_file_result:", save_url_as_file_result)

    #get_file_info_result = await client.get_file_info(example_file_path, True)
    #get_file_info_result = await client.get_file_info("", "1752", True, True)
    #print("get_file_info_result:", get_file_info_result)

    #create_download_url_result = await client.create_download_url(
    #    ["cloudreve://my/" + example_file_path]
    #)
    #print("create_download_url_result:", create_download_url_result)

    #with open(r"E:\NIL\spark\python\InoGenie\assets\AlyTay\AlyTay_00001.png", "rb") as f:
    #    new_bytes = f.read()

    #update_file_content_result = await client.update_file_content(
    #    file_uri="Spark/AlyTay_00002.png",
    #    content=new_bytes
    #)
    #print("update_file_content_result:", update_file_content_result)

    #list_files_result = await client.list_files("")
    #print("list_files_result:", list_files_result)



    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
