# Blazor Grid Error Multiple components

## Question

**Pet** asked on 31 Aug 2024

Hello Telerik, I am attempting to trial the Blazor UI. I am able to get the Telerik Button to work but not the Grid. See Error below. I have included the Repo on GitHub. Thank you for your help. GitHub Repo Multiple components use the tag 'TelerikGrid'. Components

## Answer

**Dimo** answered on 02 Sep 2024

Hi Peter, The error means that the app contains a file TelerikGrid.razor, which duplicates the name of our Grid component, which is also TelerikGrid. Please rename your . razor file. You may need to clean and rebuild the app afterwards. Regards, Dimo Progress Telerik

### Response

**Peter** commented on 03 Sep 2024

Hi Dimo, You are correct. What a silly mistake on my end. Thanks again Dimo. Peter.
