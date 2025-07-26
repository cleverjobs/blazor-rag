# Scaling Responsively

## Question

**Zhi** asked on 20 Jan 2021

Hello, Is it possible to scale the Calendar to fit the size of the screen and to have the font size, cell size etc scale responsively. As seen in the attached images, if I were to naively increase the width of the calendar to 100%: 1. The cells now have a gap in between them 2. The dates are no longer aligned to the days Thanks!

## Answer

**Marin Bratanov** answered on 20 Jan 2021

Hi Zhi Yuan, You can increase the font through CSS, and that will also enlarge the cells and text, here's a basic example (needs 2.21.0 for the Class parameter) and a screenshot of the result is attached below. I must note that the calendar is an inline-block element, so 100% width is not really part of its design purpose. <style>.large-font { font-size: 24px;
} </style> <TelerikCalendar Class="large-font" Min="@min" Max="@max" @bind-Date="@theDate"> </TelerikCalendar> <TelerikCalendar Min="@min" Max="@max" @bind-Date="@theDate"> </TelerikCalendar> @code {
private DateTime min=new DateTime(2015, 1, 1);
private DateTime max=new DateTime(2025, 12, 31);
private DateTime theDate { get; set; }=DateTime.Now;
} Regards, Marin Bratanov

### Response

**Zhi Yuan** answered on 20 Jan 2021

Thanks so much Marin! This works like a charm. On a side note, I realise that the font size modification doesn't apply to the month & year on the top left, and it also doesn't apply to the days of week. It's easy to override them using css though. :)
