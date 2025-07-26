# Blazor 2.22.0 injects a global.json of NET 5.0.101 but we are using NET 5.0.103

## Question

**SBS** asked on 24 Feb 2021

Hello, Latest 2.22.0 within the NuGet package has a content file of global.json. Is there a reason it is doing this? We use our own global.json at the solution root and want to control that for deterministic build. What I don't know is whether the client project with the Telerik NuGet dependency (and the injected global.json) is honoring your injected copy at the project level or if it uses the solution's. Either way, unless there is an explicit reason this is needed can you remove it from the package? Thank you!

## Answer

**Marin Bratanov** answered on 24 Feb 2021

Hi, Thank you for reporting this. Indeed, it should not be there and we will be working on removing it. In the meantime, could you try deleting the file to see if it goes away? On my end it does, so I wanted to see if that works for you too. Also, what problems does that cause on your end considering that, at most, it should make CLI commands run an earlier patch? Regards, Marin Bratanov

### Response

**SBSDEV** answered on 24 Feb 2021

Marin, Just tried it. I can manually delete it but it returns on package restore as you might expect :) And I don't know if it is definitively causing an issue given - if a global.json file is at the solution root I don't know if it honors that. It does appear to interfere with a dotnet publish though and it stomps over my file in the client folder. For the immediate now I will just add a command to copy mine back in between the Restore and Build steps.

### Response

**Marin Bratanov** answered on 25 Feb 2021

Hi, Could you try: clearing your local nuget cache (the easiest way is to run "dotnet nuget locals all --clear" in your terminal) cleaning the project restoring and rebuilding The goal is to remove the current package you have so it can be restored anew from our live feed where this should be fixed now. Regards, Marin Bratanov

### Response

**SBSDEV** answered on 25 Feb 2021

Worked perfectly. Thank you!

### Response

**Marin Bratanov** answered on 25 Feb 2021

Great! Thank you for confirming this for me. You will also find your Telerik points updated as a small "thank you" for bringing this up. Regards, Marin Bratanov
