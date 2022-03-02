using System;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Extensions.Logging;

namespace LT.BilledResources
{
    public class ScheduledTrigger
    {
        [FunctionName("ScheduledTrigger")]
        public void Run([TimerTrigger("0 0 7-19 * * 1-5")]TimerInfo myTimer, ILogger log)
        {
            log.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}");
        }
    }
}
