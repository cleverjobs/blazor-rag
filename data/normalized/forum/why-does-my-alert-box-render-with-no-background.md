# Why does my alert box render with no background?

## Question

**Dav** asked on 16 Feb 2023

Here is the code that calls the dialog: catch (Exception ex)
{ await Dialogs.AlertAsync(ex.Message, "Error!" );
}

### Response

**David** commented on 16 Feb 2023

Is this because we upgraded to Blazor UI 4.0.1 and the themebuilder can only build themes for version 3.6.0?

## Answer

**David** answered on 16 Feb 2023

What I had to do was go in to the Themebuilder and create a NEW project. This created a theme based on the R1 2023 components. Then I exported my .css and all was good. What I tried before was opening up my previous project, but that created a theme based on R3 2022. Since that's what that theme was originally built on.
