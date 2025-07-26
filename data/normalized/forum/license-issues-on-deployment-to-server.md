# License issues on deployment to server.

## Question

**RobRob** asked on 05 Jun 2025

We upgraded from 7.1.0 to 9.0.0 which was more difficult than it should be IMHO. We use TeamCity to do the builds. We use Octopus to do the deployments. However, the bigger issue is the new license process. I can understand Telerik's need to protect content/work from "fake malicious developers" (use that word loosely as anyone that steals software isn't really a developer), but your current license process leaves MUCH to be desired. Adding environment variables to a server? Copying license files to the server? It's pretty rare that a developer will be permitted that sort of access to a server which means a request to the server group (open a ticket) and wait and hope. Anyway, I was able to get this completed but still get the same license issue. And the file is located in the correct path. And Telerik.Licensing version 1.6.5. Added read access to C:\Telerik for IIS. Nothing, still same problem. What am I missing here? I've used the article below as reference and we still get the following: Blazor License Key - Telerik UI for Blazor I've run out of ways to try to make this work? Rob.

### Response

**Rob** commented on 05 Jun 2025

I was able to resolve the issue using the following link to point me in the right direction: Blazor License Key - Telerik UI for Blazor I added the warnings in my csproj file to prevent TeamCity from continuation of build and went thru the TC logs. In TC (TeamCity), I added a parameter of type "environment variable" and assigned the value that is in our license.txt file. Copying the license text file and setting environment variables directly on the server was NOT the way to proceed. Unfortunately, Telerik documentation was not very clear on what needed to be done. For those using TeamCity I recommend you do the TELERIK_LICENSE approach using text value.

### Response

**Dimo** commented on 06 Jun 2025

Rob - can you specify exactly which part(s) of our documentation seem to be misleading or lacking specifics?

### Response

**Rob** commented on 06 Jun 2025

Certainly, 1. Adding of the environment variable with license path or value. You don't qualify where this should happen, local PC or IIS server or build server or all? 2. You don't specify the process in a single flow, it's disjointed. Suggest you have a flow for each use case and don't combine them into and/or steps in one global flow. 3. Need to make it clear that getting the license file installed on local isn't enough for the 99% use case. Deployments need to be addressed, this is not made clear as a "must do" (it's not optional). I eventually discovered how to get your license process working, but that was thanks to Google AI and not Telerik documentation. For future: For those of us that login to the Telerik URL to get packages, we should automatically be license verified (Telerik has our renewal data and license information). To be fair, I have tried removing my local license file to see if I can still build local ... maybe it's not needed local? Telerik is the ONLY 3rd party tool I've used that has now required server or build level special parameters for deployment. I don't see how or why this is needed at the deployment level? It certainly has our IT folks raising their heckles ... they really don't like it. There has to be a better way to protect you work/content? Rob.

### Response

**Dimo** commented on 06 Jun 2025

Thanks, Rob! OK, the essence is that a license key is required by environments which build and publish apps. I will try to accommodate your feedback next week.>> For those of us that login to the Telerik URL to get packages, we should automatically be license verified This does not cover all possible scenarios. For example, you can rely on NuGet cache or a local NuGet feed instead of a live NuGet server. You may also have a subscription license that limits the time frame in which you can build and publish apps.>> I don't see how or why this is needed at the deployment level? This is because a license key is required during build and publish. If you publish your app to a folder on your local dev machine, and then copy the assets to a web server, then you will only need a license key on your local dev machine.>> There has to be a better way to protect you work/content? Do you have specific suggestions?
