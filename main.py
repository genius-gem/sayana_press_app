
import webview


WEBSITE_URL = "https://sayanapress.com.ng"


def main():
    webview.settings["OPEN_EXTERNAL_LINKS_IN_BROWSER"] = True
    webview.settings["ALLOW_DOWNLOADS"] = True

    webview.create_window(
        "Sayana Press",
        WEBSITE_URL
    )

    webview.start()


if __name__ == "__main__":
    main()
