# py - ios: A Wrapper for iOS Device Interaction Tools Based on the go - ios Project

-   [English](#Installation)
-   [中文版](#安装)

For the Chinese version of this README, please refer to [here](LINK_TO_CHINESE_README). (Please replace `LINK_TO_CHINESE_README` with the actual link to the Chinese README file.)

`py-ios` is a feature - rich command - line tool that is simply wrapped based on the [https://github.com/danielpaulus/go - ios](https://github.com/danielpaulus/go - ios) project. It simplifies the process of interacting with iOS devices, providing a user - friendly interface for a wide range of operations.

## Installation
The specific steps for installing `py - ios` depend on your environment. Usually, you can install it via a package manager (such as `pip`):
```bash
pip install py - ios
```
Make sure your system meets the dependency requirements of `py - ios`. The required dependency libraries may be automatically installed during the installation process.

## Usage
`py - ios` offers numerous sub - commands, each with a specific function. You can view all available sub - commands and their brief descriptions by using `idb --help`. Here are the detailed introductions of some commonly used sub - commands:

### Device Information and Management
- **Check Version**:
  ```bash
  idb --version
  ```
  This command is used to view the current version number of `py - ios`.
- **Activate Device**:
  ```bash
  idb activate
  ```
  Attempt to activate the connected iOS device. The activation process may require meeting specific conditions, such as the device being paired and conforming to the activation policy.
- **Get Device Name**:
  ```bash
  idb devicename
  ```
  Returns the name of the connected iOS device.
- **View Device State List**:
  ```bash
  idb devicestate list
  ```
  Displays various current state information of the device, such as whether the device is locked and the battery status.
- **Enter Development Mode**:
  ```bash
  idb devmode enable
  ```
  Enables the device's development mode, which is necessary for some advanced debugging and development operations.
- **Reboot Device**:
  ```bash
  idb reboot
  ```
  Reboots the connected iOS device.

### Application Management
- **List Applications**:
  ```bash
  idb apps
  ```
  Lists the applications installed on the device. You can use the `--system` option to list system applications, the `--all` option to list all applications (including system applications), the `--list` option to output in a concise list form, and the `--filesharing` option to list applications that support file sharing.
- **Install Application**:
  ```bash
  idb install --path=path/to/ipaOrAppFolder
  ```
  Installs the IPA file or application folder at the specified path onto the device.
- **Launch Application**:
  ```bash
  idb launch bundleID
  ```
  Launches the application with the specified Bundle ID. You can use the `--wait` option to wait for the application to start up completely, the `--kill - existing` option to kill the running application with the same name before launching, and the `--arg` and `--env` options to pass parameters and environment variables to the application.
- **Uninstall Application**:
  ```bash
  idb uninstall bundleID
  ```
  Uninstalls the application with the specified Bundle ID.
- **Get Application File System Synchronization**:
  ```bash
  idb fsync --app=bundleId pull --srcPath=srcPath --dstPath=dstPath
  idb fsync --app=bundleId push --srcPath=srcPath --dstPath=dstPath
  ```
  Use `pull` to pull files or directories from the application sandbox to the local machine, and use `push` to push local files or directories to the application sandbox. It also supports operations such as `rm` (delete), `tree` (view directory structure), and `mkdir` (create directory).

### Debugging and Diagnosis
- **Debug Application**:
  ```bash
  idb debug app_path
  ```
  Launches a debugging session for the specified application. You can use the `--stop - at - entry` option to pause debugging at the application's entry point.
- **View Crash Logs**:
  ```bash
  idb crash ls
  ```
  Lists the crash logs on the device. You can filter the logs through `<pattern>`.
  ```bash
  idb crash cp srcpattern target
  ```
  Copies the crash logs that match `<srcpattern>` to the `<target>` directory.
  ```bash
  idb crash rm cwd pattern
  ```
  Deletes the crash logs that match `<pattern>` in the `<cwd>` directory.
- **View System Logs**:
  ```bash
  idb syslog
  ```
  Views the device's system logs in real - time. Using the `--parse` option can parse and format the logs for output.
- **List Device Diagnostic Information**:
  ```bash
  idb diagnostics list
  ```
  Displays various diagnostic information of the device, such as hardware status and software version.

### System Settings and Function Operations
- **Set Language**:
  ```bash
  idb lang --setlocale=locale --setlang=newlang
  ```
  Sets the language and region settings of the device.
- **Set Date**:
  ```bash
  idb date
  ```
  Can be used to set the device's date and time (the specific setting method may vary depending on command options).
- **Assistive Function Operations**:
  ```bash
  idb assistivetouch enable
  idb assistivetouch disable
  idb assistivetouch toggle
  idb assistivetouch get
  ```
  These commands are used to enable, disable, toggle, and obtain the status of the AssistiveTouch function respectively. Similarly, the `voiceover` and `zoom` sub - commands can perform the same operations on the VoiceOver and zoom functions.
- **Location Simulation**:
  ```bash
  idb setlocation --lat=lat --lon=lon
  ```
  Sets the simulated location coordinates of the device.
  ```bash
  idb setlocationgpx --gpxfilepath=gpxfilepath
  ```
  Uses a GPX file to simulate the device's location trajectory.
- **HTTP Proxy Settings**:
  ```bash
  idb httpproxy host port user pass --p12file=orgid --password=p12password
  ```
  Sets the device's HTTP proxy.
  ```bash
  idb httpproxy remove
  ```
  Removes the device's HTTP proxy settings.

### Network - related
- **Port Forwarding**:
  ```bash
  idb forward hostPort targetPort
  ```
  Forwards the `<targetPort>` port of the device to the `<hostPort>` port of the host, facilitating access to services within the device on the host.
- **Network Traffic Capture**:
  ```bash
  idb pcap
  ```
  Captures the device's network traffic. You can use the `--pid` or `--process` option to specify capturing the traffic of a specific process.
- **Get Device IP Address**:
  ```bash
  idb ip
  ```
  Obtains the current IP address of the device.

### Other Functions
- **Device Pairing**:
  ```bash
  idb pair --p12file=orgid --password=p12password
  ```
  Uses the specified P12 file and password to pair the device.
- **Read Pairing Information**:
  ```bash
  idb readpair
  ```
  Reads the pairing information of the device.
- **Run Tests**:
  ```bash
  idb runtest --bundle - id=bundleid --test - runner - bundle - id=testrunnerbundleid --xctest - config=xctestconfig
  ```
  Runs the tests of an iOS application. You can specify the test Bundle ID, the test runner Bundle ID, and the XCTest configuration file, etc.

## Examples
1. Install an application named `MyApp.ipa` onto the device:
  ```bash
  idb install --path=MyApp.ipa
  ```
2. Launch the `com.example.MyApp` application and pass the parameter `--arg=value` and the environment variable `--env=ENV_VAR=value`:
  ```bash
  idb launch com.example.MyApp --arg=value --env=ENV_VAR=value
  ```
3. Pull the `Documents` directory from the sandbox of the `com.example.MyApp` application on the device to the `~/Downloads/MyAppDocuments` directory on the local machine:
  ```bash
  idb fsync --app=com.example.MyApp pull --srcPath=Documents --dstPath=~/Downloads/MyAppDocuments
  ```

For the Chinese version of this README, please refer to [here](LINK_TO_CHINESE_README). (Please replace `LINK_TO_CHINESE_README` with the actual link to the Chinese README file.)


`py-ios` 是一款功能丰富的命令行工具，它基于 [https://github.com/danielpaulus/go-ios](https://github.com/danielpaulus/go-ios) 项目进行简单封装

## 安装
安装 `py-ios` 的具体步骤取决于你的环境。通常，你可以通过包管理器（如 `pip`）进行安装：
```bash
pip install py-ios
```
确保你的系统满足 `py-ios` 的依赖要求，安装过程中可能会自动安装所需的依赖库。

## 用法
`py-ios` 提供了众多子命令，每个子命令都有特定的功能。你可以通过 `idb --help` 查看所有可用的子命令及其简要描述。以下是一些常用子命令的详细介绍：

### 设备信息与管理
- **查看版本**：
  ```bash
  idb --version
  ```
  该命令用于查看 `py-ios` 的当前版本号。
- **激活设备**：
  ```bash
  idb activate
  ```
  尝试激活连接的iOS设备。激活过程可能需要满足特定的条件，如设备已配对且符合激活策略。
- **获取设备名称**：
  ```bash
  idb devicename
  ```
  返回连接的iOS设备的名称。
- **查看设备状态列表**：
  ```bash
  idb devicestate list
  ```
  显示设备当前的各种状态信息，如设备是否锁定、电池状态等。
- **进入开发模式**：
  ```bash
  idb devmode enable
  ```
  开启设备的开发模式，这对于一些高级调试和开发操作是必要的。
- **重启设备**：
  ```bash
  idb reboot
  ```
  重启连接的iOS设备。

### 应用管理
- **列出应用**：
  ```bash
  idb apps
  ```
  列出设备上安装的应用。可通过 `--system` 选项列出系统应用，`--all` 选项列出所有应用（包括系统应用），`--list` 以简洁列表形式输出，`--filesharing` 列出支持文件共享的应用。
- **安装应用**：
  ```bash
  idb install --path=path/to/ipaOrAppFolder
  ```
  安装指定路径的IPA文件或应用文件夹到设备上。
- **启动应用**：
  ```bash
  idb launch bundleID
  ```
  启动指定Bundle ID的应用。可使用 `--wait` 选项等待应用启动完成，`--kill-existing` 选项在启动前杀死正在运行的同名应用，`--arg` 和 `--env` 用于传递参数和环境变量给应用。
- **卸载应用**：
  ```bash
  idb uninstall bundleID
  ```
  卸载指定Bundle ID的应用。
- **获取应用文件系统同步**：
  ```bash
  idb fsync --app=bundleId pull --srcPath=srcPath --dstPath=dstPath
  idb fsync --app=bundleId push --srcPath=srcPath --dstPath=dstPath
  ```
  使用 `pull` 从应用沙盒中拉取文件或目录到本地，使用 `push` 将本地文件或目录推送到应用沙盒中。还支持 `rm`（删除）、`tree`（查看目录结构）、`mkdir`（创建目录）等操作。

### 调试与诊断
- **调试应用**：
  ```bash
  idb debug app_path
  ```
  启动对指定应用的调试会话。可使用 `--stop-at-entry` 选项在应用入口处暂停调试。
- **查看崩溃日志**：
  ```bash
  idb crash ls
  ```
  列出设备上的崩溃日志。可通过 `<pattern>` 来过滤日志。
  ```bash
  idb crash cp srcpattern target
  ```
  将匹配 `<srcpattern>` 的崩溃日志复制到 `<target>` 目录。
  ```bash
  idb crash rm cwd pattern
  ```
  删除在 `<cwd>` 目录下匹配 `<pattern>` 的崩溃日志。
- **系统日志查看**：
  ```bash
  idb syslog
  ```
  实时查看设备的系统日志。使用 `--parse` 选项可对日志进行解析和格式化输出。
- **设备诊断信息列表**：
  ```bash
  idb diagnostics list
  ```
  显示设备的各种诊断信息，如硬件状态、软件版本等。

### 系统设置与功能操作
- **设置语言**：
  ```bash
  idb lang --setlocale=locale --setlang=newlang
  ```
  设置设备的语言和区域设置。
- **设置日期**：
  ```bash
  idb date
  ```
  可用于设置设备的日期和时间（具体设置方式可能因命令选项而异）。
- **辅助功能操作**：
  ```bash
  idb assistivetouch enable
  idb assistivetouch disable
  idb assistivetouch toggle
  idb assistivetouch get
  ```
  分别用于启用、禁用、切换和获取AssistiveTouch功能的状态。类似地，`voiceover` 和 `zoom` 子命令也可对VoiceOver和缩放功能进行相同操作。
- **位置模拟**：
  ```bash
  idb setlocation --lat=lat --lon=lon
  ```
  设置设备的模拟位置坐标。
  ```bash
  idb setlocationgpx --gpxfilepath=gpxfilepath
  ```
  使用GPX文件来模拟设备的位置轨迹。
- **HTTP代理设置**：
  ```bash
  idb httpproxy host port user pass --p12file=orgid --password=p12password
  ```
  设置设备的HTTP代理。
  ```bash
  idb httpproxy remove
  ```
  移除设备的HTTP代理设置。

### 网络相关
- **端口转发**：
  ```bash
  idb forward hostPort targetPort
  ```
  将设备的 `<targetPort>` 端口转发到主机的 `<hostPort>` 端口，方便在主机上访问设备内的服务。
- **网络流量捕获**：
  ```bash
  idb pcap
  ```
  捕获设备的网络流量。可通过 `--pid` 或 `--process` 选项指定捕获特定进程的流量。
- **设备IP地址获取**：
  ```bash
  idb ip
  ```
  获取设备当前的IP地址。

### 其他功能
- **设备配对**：
  ```bash
  idb pair --p12file=orgid --password=p12password
  ```
  使用指定的P12文件和密码对设备进行配对。
- **读取配对信息**：
  ```bash
  idb readpair
  ```
  读取设备的配对信息。
- **运行测试**：
  ```bash
  idb runtest --bundle-id=bundleid --test-runner-bundle-id=testrunnerbundleid --xctest-config=xctestconfig
  ```
  运行iOS应用的测试。可指定测试Bundle ID、测试运行器Bundle ID以及XCTest配置文件等。

## 示例
1. 安装一个名为 `MyApp.ipa` 的应用到设备上：
  ```bash
  idb install --path=MyApp.ipa
  ```
2. 启动 `com.example.MyApp` 应用，并传递参数 `--arg=value` 和环境变量 `--env=ENV_VAR=value`：
  ```bash
  idb launch com.example.MyApp --arg=value --env=ENV_VAR=value
  ```
3. 从设备上拉取 `com.example.MyApp` 应用沙盒中的 `Documents` 目录到本地的 `~/Downloads/MyAppDocuments` 目录：
  ```bash
  idb fsync --app=com.example.MyApp pull --srcPath=Documents --dstPath=~/Downloads/MyAppDocuments
  ```
