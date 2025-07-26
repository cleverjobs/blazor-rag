# Can't install telerik.ui.for.blazor.6.0.0.commercial

## Question

**Mic** asked on 27 May 2024

Trying to install from telerik.ui.for.blazor.6.0.0.commercial.msi on Windows 11 running on Parallels Desktop 19 for MAC. The Mac host is a Macbookpro with the Apple M2 Pro chip. The error message is: This application requires .NET SDK 6.0 or later. Please install... I have the following sdks installed: 7.0.409 [C:\Program Files\dotnet\sdk] 8.0.300 [C:\Program Files\dotnet\sdk] I was able to unzip the telerik.ui.for.blazor.6.0.0.commercial.zip file to the destination and reference the folder from VisualStudio 2022 and all seems to be well. Just wondering should it be possible to install from the .msi Many thanks, Michael.

### Response

**Chris** commented on 28 May 2024

Same problem. I installed .NET 6 sdk but still broken. Mine is a M3.

## Answer

**Nansi** answered on 29 May 2024

Hi Michael, I tested the scenario on my side. I deleted the.NET SDK 6.0, and the installation of the telerik.ui.for.blazor.6.0.0.commercial.msi succeeded without errors. However, we are not testing the installation on virtual machines. There can be some specifics we are not aware of. We did have a previous customer who encountered the same error on Parallels, but they didn't provide us with more information. It would be very helpful if you could generate log file and send it to us for review. You could do this by following these steps: Start Command Prompt as Administrator Run the command "msiexec /i [path_to_installer] -l*v [path_to_log_file]" It's enough to just start the installer and see the initial page, so you could cancel it and send us the log file in a zip archive For example if the command prompt is navigated to the installer folder: "msiexec /i telerik.ui.for.blazor.6.0.0. commercial.msi -l*v log.txt" - this will generate the log.txt in the same folder from which the command is executed. Add the log.txt to a zip archive and send it as an attachment to a message here. You could also try to workaround this specific issue by following these steps: Start Command Prompt as Administrator Run the command "msiexec /i [path_to_installer] REQUIREDDOTNETCORESDKINSTALLED=1" For example if the command prompt is navigated to the installer folder: "msiexec /i telerik.ui.for.blazor. 6.0.0. commercial.msi REQUIREDDOTNETCORESDKINSTALLED=1 " Passing the "REQUIREDDOTNETCORESDKINSTALLED=1" should let you pass the prerequisite check and let you install and use the product. Let me know how it goes. Regards, Nansi Progress Telerik

### Response

**Michael** commented on 29 May 2024

Hi Nansi, I went for the workaround of specifying "REQUIREDDOTNETCORESDKINSTALLED=1" and everything seems to have installed OK, thanks for that! I am attaching the zip file of the log of trying to run the installer without the above flag, which failed as before. Please note that I did this after installing the package correctly, but the install failed with the same message as before. Also, I have removed the username and user SID from the log file. Hope this helps and many thanks, Michael.

### Response

**Momchil** commented on 31 May 2024

Hi Michael, Thank you for providing the log file. It seems that our installer has
an issue detecting the installed .NET versions on machines running on
ARM-based processors. We will look into this and improve it for
one of our next releases. In the meantime you could use the workaround to
install the product successfully.

### Response

**Michael** commented on 31 May 2024

No problem. Many thanks.
