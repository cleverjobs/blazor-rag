# TelerikLoader with secondary theme colour doesn't display correct colour in any theme

## Question

**Pin** asked on 18 Oct 2022

Hey, So I noticed that the Telerik Loader isn't displaying the correct colour when you set the ThemeColor on it to the secondary colour, seemingly in any of the themes. Here's a REPL I made, where each theme color is used, and I placed a button right next to each loader for easy comparison: [https://blazorrepl.telerik.com/mGbYbMYa13VfwDlm06](https://blazorrepl.telerik.com/mGbYbMYa13VfwDlm06) Try changing the theme and running the repl again and you will notice it is consistently displaying as a very different colour to the button. In this screenshot, the loader for Secondary is dark, whereas the button is much lighter. This appears to be an issue in all the themes I selected, but this screenshot shows the default theme. Notice, that all other loaders and buttons match at all times in all themes.

## Answer

**Dimo** answered on 20 Oct 2022

Hello Matthew, I agree that a single discrepancy may look like an oversight, but it's actually by design. The Button's background is lighter on purpose, otherwise it will require light text color, i.e. inverse design. Regards, Dimo Progress Telerik

### Response

**Pingu** commented on 20 Oct 2022

Hi Dimo, I wasn't aware of that, however I still feel like there is an issue here. Try it in other themes for example... The Main material theme has pink as the secondary colour yet its still a dark colour for the loader colour... Doesn't seem to follow the reasoning given above and doesn't match at all.

### Response

**Dimo** commented on 21 Oct 2022

OK, these look too different indeed. I sent an inquiry to our designers and will log a bug report on your behalf if necessary. In the meantime, the other option is to override our theme and set the colors you prefer: .k-loader-secondary.k-loader-segment,.k-button.k-button-solid-secondary { background-color: pink;
}

### Response

**Dimo** commented on 28 Oct 2022

Matthew, so I confirm the current colors are incorrect. The designers and front-enders will revise them for some of the coming releases. Thanks for reporting the inconsistency! I am awarding you some Telerik points.
