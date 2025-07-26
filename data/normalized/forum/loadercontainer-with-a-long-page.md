# LoaderContainer with a long page?

## Question

**Dea** asked on 30 Jan 2023

How does one move the text msg & animation higher up the page? It seems to default to the center of the page. Example: I would like that animation and the text message up near the top of the page. Code: @* LoaderContainer with transparent panel *@<TelerikLoaderContainer Class="no-panel" ThemeColor="@ThemeConstants.Loader.ThemeColor.Dark" /> <style> .no-panel.k-loader-container-panel { background-color: transparent; border-width: 0; } </style> <TelerikGridLayout> <GridLayoutColumns> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="7%"></GridLayoutColumn> </GridLayoutColumns> <GridLayoutRows> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="400px"></GridLayoutRow> </GridLayoutRows> </TelerikGridLayout> Those heights are to simulate my long page :).

### Response

**Deasun** commented on 01 Feb 2023

That did not fix the issue. In fact it made it worse. :( position: fixed; in the style area made the text msg and animation disappear! @* LoaderContainer with transparent panel *@<TelerikLoaderContainer Class="no-panel" ThemeColor="@ThemeConstants.Loader.ThemeColor.Dark" /> <style> .no-panel.k-loader-container-panel { background-color: transparent; border-width: 0; position: fixed; } </style> <TelerikGridLayout> <GridLayoutColumns> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="6%"></GridLayoutColumn> <GridLayoutColumn Width="7%"></GridLayoutColumn> </GridLayoutColumns> <GridLayoutRows> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="100px"></GridLayoutRow> <GridLayoutRow Height="400px"></GridLayoutRow> </GridLayoutRows> </TelerikGridLayout>

### Response

**Dimo** commented on 01 Feb 2023

My suggestion was to apply position:fixed to the LoaderContainer class itself, and not on some internal elements. There is a big difference. div.no-panel { position: fixed;
}.no-panel.k-loader-container-panel { background-color: transparent; border-width: 0;
}

## Answer

**Dimo** answered on 01 Feb 2023

Hi Deasun, The default behavior of the LoaderContainer height is to match the viewport height. If this is not the case on your side, maybe the page <body> has a position:relative style or something like that. In this case, apply a position:fixed style to the LoaderContainer. Regards, Dimo
