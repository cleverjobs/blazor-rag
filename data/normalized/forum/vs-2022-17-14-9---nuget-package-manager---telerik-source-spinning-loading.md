# VS 2022 17.14.9 - NuGet Package Manager - Telerik source spinning "Loading"?

## Question

**RobRob** asked on 15 Jul 2025

I just get a spinning wheel when I bring up NuGet Package Manager and have the source set to Telerik. If I select other package sources they load and display quickly. Any suggestions?

### Response

**Dimo** commented on 16 Jul 2025

Hi Rob, Our NuGet server appears to be fully operational in the last 24 hours. Does the observed behavior occur sometimes or always? Do you get an error in the Visual Studio Package Manager Console? Do any packages display after some delay? Can you test from another network / internet provider?

### Response

**Rob** commented on 17 Jul 2025

Always. No errors reported as the "Loading..." never completes or times-out (was expecting at least a timeout). None of the Telerik packages display. Internet is working by evidence the other Package Sources (not Telerik) do display but also by evidence of Speed Test (google) and my other activity, like me reporting the issue on your website.

### Response

**Dimo** commented on 18 Jul 2025

Hi Rob, OK, thanks. Can you connect to our NuGet server from the web browser? Can you verify that your credentials are correct? Can you test from another network? Are you using a proxy?

### Response

**Rob** commented on 24 Jul 2025

Hi Dimo, I had modified my Telerik login (changed my password as per our company policy). Apparently this requires that I load the Windows Credentials Manager and I modified (Edit) the password for VS_Telerik to my new password and that resolved the issue.

## Answer

**Rob** answered on 24 Jul 2025

See Dimo post for solution:
