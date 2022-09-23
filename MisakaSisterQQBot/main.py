import pkgutil

from graia.ariadne.app import Ariadne
from graia.ariadne.model import MiraiSession
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour
from graia.scheduler import GraiaScheduler
from graia.scheduler.saya import GraiaSchedulerBehaviour

app = Ariadne(
    MiraiSession(
        # 以下3行请按照你的 MAH 配置来填写
        host="http://localhost:32767",  # 同 MAH 的 port
        verify_key="ComputerParts",  # 同 MAH 配置的 verifyKey
        account=1905316697,  # 机器人 QQ 账号
    ),
)
app.create(GraiaScheduler)
saya = app.create(Saya)
saya.install_behaviours(
    app.create(BroadcastBehaviour),
    app.create(GraiaSchedulerBehaviour),
)

with saya.module_context():
    for module_info in pkgutil.iter_modules(["modules"]):
        if module_info.name.startswith("_"):
            continue
        if module_info.name == "test":
            continue
        saya.require("modules." + module_info.name)

app.launch_blocking()