<div align="center">
  <img
    style="width: 165px; height: 165px"
    src="https://raw.githubusercontent.com/FireHead90544/AnimeRPC/main/logo.png"
    title="AnimeRPC"
    alt="AnimeRPC"
  />
  <h3>AnimeRPC</h3>
  <p>
    A discord Rich Presence Client for showing Anime info on your discord profile.
  </p>
  <a href="https://github.com/FireHead90544/AnimeRPC/releases"> <strong>· Download Executable Release ·</strong></a>
</div>
<hr>

### Features
- Clean UI
- Anime Info on RPC
- Shows Anime Name/Release Date
- A Button Linked To The Anime's Watch Page
- Dynamic Cover Images (Automatically Fetches)
- Scrapes GogoAnime
- **Note: Not a feature, There are no ratelimits check, so you are adviced to not update presence too frequently (wait at least ~90 seconds)**

### Installation

The simplest way to install `AnimeRPC` is to download the pre-built release (windows only) from here: [Download Latest Release](https://github.com/FireHead90544/AnimeRPC/releases/latest).

- Linux/Mac users need to build the binaries themselves, clone the repo, create a virtualenv (recommended but optional), install the requirements. Run the below command to build the binary. The output would be in `dist/` directory. [Optionally, instead of `--onefile` flag you can use `--onedir` for faster app launch.]

```console
pyinstaller --onefile --noconfirm --console --name AnimeRPC --icon logo.ico rpc.py
```

### Screenshots/Usage
- Run the executable or python file, follow the instructions.

![AnimeRPC](https://user-images.githubusercontent.com/55452780/185986480-56a87fc2-380d-455d-a32c-d6398ab7e9cf.png)

### License
[Do What The F\*ck You Want To](https://github.com/FireHead90544/AnimeRPC/blob/main/LICENSE), You are free to do anything, just don't eat my brain :)
