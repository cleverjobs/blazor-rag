# Resize Carousel when Window is maximized

## Question

**Joh** asked on 22 Oct 2024

Is it possible to get the carousel to maximize when you maximize the window? Currently, the carousel retains its actual size when the window is maximized. <TelerikWindow @ref="ImageWindow" Class="demo-window" Width="fit-content" Height="fit-content" Centered="true" Modal="true" @bind-Visible="@IsImageWindowVisible" FooterLayoutAlign="@WindowFooterLayoutAlign.Start">
<WindowTitle>
<strong>View Image</strong>
</WindowTitle>
<WindowActions>
<WindowAction Name="Close"></WindowAction>
</WindowActions>
<WindowContent>
<TelerikCarousel Data="@ListViewData" Width="@(CarouselWidth + " vw ")" Height="@(" calc( " + CarouselWidth + " vw *.75 ) ")" Pageable="false" LoopPages="false" AutomaticPageChange="false" @bind-Page="@CarouselPageIndex">
<Template>
<div class="image-with-text">
<p>@(context.Description)</p>
<img src="@(context.FileUrl)" alt="ReportImage" />
</div>
</Template>
</TelerikCarousel>
</WindowContent>
</TelerikWindow>
