# Update the grid when data changes on the server - SignalR

## Question

**Mar** asked on 07 Feb 2023

I have a grid with stock prices. The server is listen to a message bus for new prices. Then it send the prices using SignalR to all connected clients. How can I upgrade the grid so it easy to see which rows has changed? In some programs I have seen some animations effects.

## Answer

**Nadezhda Tacheva** answered on 10 Feb 2023

Hi Martin, As I understand you have successfully configured the Grid to update its items based on the received data and you are currently looking for an option to better indicate the changes to the user (please let me know if I am missing something). I imagine you'd need some visual indication similar to the one we have implemented in our stocks demo: [https://demos.telerik.com/blazor-financial-portfolio/real-time.](https://demos.telerik.com/blazor-financial-portfolio/real-time.) See how the Price and Change cells content is flashing and changing its color depending on the price change. You can achieve such functionality by conditionally adding CSS classes to the desired cells depending on your logic (e.g. price change in the context of the stocks). In the example I shared, such a custom class is added to the span element inside the cell template of the specific cells: [https://github.com/telerik/blazor-ui/blob/master/sample-applications/blazor-stocks/Client/Pages/RealTime.razor#L30.](https://github.com/telerik/blazor-ui/blob/master/sample-applications/blazor-stocks/Client/Pages/RealTime.razor#L30.) We track the price change to apply the corresponding class - "price-up" or "price-down". These classes apply different font colors. In addition, they also apply animation to achieve this flashing effect. You may incorporate a similar approach in your application. In case you are not using cell templates, you may subscribe to the OnCellRender event of the Grid to apply the desired classes. If you want to customize the whole row and not certain cells, you may use the OnRowRender event. I hope you will find the above information useful to move forward with your application. Please let us know if any further questions appear. Regards, Nadezhda Tacheva

### Response

**Martin Herløv** commented on 10 Feb 2023

Thanks a gazillion 😊The answer is spot on. I think Telerik has the best support for any component vendor
