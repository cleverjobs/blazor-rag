# Locked Multicolumn-Header breaks layout since version 4.6

## Question

**TimTim** asked on 21 Nov 2023

Hi there, when using a Grid with a multicolumn header which is locked, the layout breaks on horizontal scolling. This behavior appears since Telerik UI Version 4.6 and also remains in 5.0. See REPL sample below (just use horizontal scroll) [https://blazorrepl.telerik.com/wRPvclYX432myApT30](https://blazorrepl.telerik.com/wRPvclYX432myApT30) When switching to Version 4.5 the grid acts as expected. One more interesting thing I observed is, if you resize the column at runtime (for the verions 4.6 and 5.0) the grid also acts as expected. Feels like there is some refresh or initial rerendering of the component missing. Any ideas on that?

## Answer

**Nadezhda Tacheva** answered on 22 Nov 2023

Hi Tim, Thank you for reporting the behavior! This is essentially a regression and I have opened a report in our feedback portal on your behalf: [Regression] Locked Multi-Column Header breaks layout when scrolling horizontally. I added your vote there and as a creator, you are automatically subscribed to get status updates. We place the regressions directly in our backlog with the highest possible priority. Unfortunately, there is no reliable workaround for the time being other than not locking the columns in this scenario. Last but not least, I updated your Telerik points as a small gesture of appreciation for your report. Regards, Nadezhda Tacheva Progress Telerik
