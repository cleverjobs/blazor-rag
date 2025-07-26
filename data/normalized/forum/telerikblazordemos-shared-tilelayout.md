# TelerikBlazorDemos.Shared.TileLayout

## Question

**Nei** asked on 17 Sep 2020

Where can I get a hold of these files? Looks like all the CSS for this demom in there, would be good of these were in a tab at the top like the old ajax demos used to be

## Answer

**Marin Bratanov** answered on 17 Sep 2020

Hi Neil, They are in the project that you can find in the "demos" folder of your local installation. The path matches the namespace, as with components by default. I am also attaching a short video that shows how you can see the relevant source code. If there is demo-specific CSS it is in inline <style> tags in the demo component. The Overview demo of the TileLayout does not have styles, and the shared styles used by the entire app are referenced from its wwwroot folder. Regards, Marin Bratanov
