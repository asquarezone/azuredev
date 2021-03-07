using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(SecureWeb.Startup))]
namespace SecureWeb
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
