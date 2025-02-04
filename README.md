### **Installing FFmpeg on Windows**

Follow these steps to install FFmpeg on Windows:

1. **Download FFmpeg**:
    - Visit the official FFmpeg website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
    - Download the **Windows build** from the **Windows builds by BtbN** section, which will provide a ZIP file.

2. **Extract the ZIP File**:
    - Once the ZIP file is downloaded, extract it to a folder of your choice. For example, extract it to `C:\ffmpeg`.

3. **Add FFmpeg to the System PATH**:
    - Navigate to the folder where you extracted FFmpeg (e.g., `C:\ffmpeg`).
    - Inside the FFmpeg folder, locate the **`bin`** folder, which contains the `ffmpeg.exe` file.
    - Copy the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).
    - Open **System Properties**:
        - Press `Win + X`, select **System** (or go to **Control Panel** → **System and Security** → **System**).
        - Click on **Advanced system settings** on the left side of the window.
        - In the **System Properties** window, click on the **Environment Variables** button.
    - In the **Environment Variables** window:
        - Under **System variables**, scroll down and select the **Path** variable, then click **Edit**.
        - Click **New** and paste the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).
        - Click **OK** to save your changes.

4. **Verify FFmpeg Installation**:
    - Open **Command Prompt** (press `Win + R`, type `cmd`, and press Enter).
    - Type the following command and press Enter:
      ```bash
      ffmpeg -version
      ```
    - If FFmpeg is properly installed, you will see version information for FFmpeg in the terminal.

### **Using FFmpeg in Your Project**

After following the steps above, FFmpeg will be installed on your system, and you can use it in your scripts and commands. The project will automatically detect FFmpeg, so you don't need to specify its location manually.

---

```
// Setup
// install python
// create venv 
python3.13 -m venv venv
source venv/Script/activate
source venv/bin/activate


// install requirements
pip install -r requirements.txt

// Download soptify paylist:
python download.py 

```

