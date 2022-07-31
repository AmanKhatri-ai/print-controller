import wget

def fileDownload(url, filepath):
    '''
    Downloads a file from the given URL and store the file into filesystem

    Parameters:
        url: File download URL
        filepath: Location to store the file, filename should have file extension also

    Returns:
        The downloaded file path
    '''
    print(f"[DOWNLOADER] Downloading model file...")
    print(f"[DOWNLOADER] URL: { url }")

    response = wget.download(url, filepath)

    print()
    print(f"[DOWNLOADER] Model file downloaded")
    print(f"[DOWNLOADER] File: { response }")

    return response
