import asyncio

from src.inocloudreve import CloudreveClient

async def main():
    client = CloudreveClient()

    client.init(
        base_url= ""
    )

    ping_result = await client.ping()
    print("Ping response:", ping_result)

    password_login_result = await client.password_sign_in(
        email="",
        password=""
    )
    print("password_login_result:", password_login_result)
    print("is_token_valid:", client.is_token_valid())

    download_file_result = await client.download_file(
        path_to_save=r"",
        uri="",
        archive=False,
        no_cache=True,
    )
    print("download_file_result:", download_file_result)

    #upload_file_result = await client.upload_file(
    #    local_path=r"",
    #    remote_path=f"",
    #    storage_policy=""
    #)
    #print("upload_file_result:", upload_file_result)

    #generate_token_result = client.generate_token(
    #    master_key=master_key,
    #    user_id=""
    #)
    #print("generate_token_result:", generate_token_result)
    #print("is_token_valid:", client.is_token_valid())

    #decode_token_result = client.decode_token(
    #    master_key=master_key,
    #    access_token=generate_token_result["token"]["access_token"]
    #)
    #print("decode_token_result:", decode_token_result)

    #print(password_login_result["token"]["access_token"])

    #decode_token2_result = client.decode_token(
    #    master_key=master_key,
    #    access_token=password_login_result["token"]["access_token"]
    #)
    #print("decode_token_result:", decode_token2_result)

    #get_last_folder_result = await client.get_last_folder_or_file(uri="")
    #print("get_last_folder_result:", get_last_folder_result["data"])

    #refresh_token_result = await client.refresh_token()
    #print ("refresh_token_result:",refresh_token_result)

    #example_file_path = ""
    #example_file_path = ""
    #example_file_path = ""

    #result = await client.get_download_url(example_file_path, True)
    #print("result:", result)
    #print("url:", result["url"])

    #save_url_as_file_result = await client.save_url_as_file(
    #    result["url"],
    #    r"",
    #    result["file_name"],
    #    result["extension"])
    #print("save_url_as_file_result:", save_url_as_file_result)

    #get_file_info_result = await client.get_file_info(example_file_path, True)
    #get_file_info_result = await client.get_file_info("", "", True, True)
    #print("get_file_info_result:", get_file_info_result)

    #create_download_url_result = await client.create_download_url(
    #    ["cloudreve://my/" + example_file_path]
    #)
    #print("create_download_url_result:", create_download_url_result)


    #read_file_as_bytes = client.read_file_as_bytes(r"")
    #update_file_content_result = await client.update_file_content(
    #    file_uri="",
    #    content=read_file_as_bytes["data"]
    #)

    #print("update_file_content_result:", update_file_content_result)

    #list_files_result = await client.list_files("")
    #print("list_files_result:", list_files_result)

    #create_upload_session_result = await client.create_upload_session("", , "")
    #print("create_upload_session_result:", create_upload_session_result)

    #delete_upload_session_result = await client.delete_upload_session(
    #    "",
    #    "")
    #print("delete_upload_session_result:", delete_upload_session_result)

    #delete_file_result = await client.delete_file([""])
    #print("delete_file_result:", delete_file_result)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
