from nonebot import on_command, CommandSession, permission as perm, logger
from .StateMachine import NGFSM
from .RecieveFromPrivate import SetNG
from copy import copy



@on_command('NG词语游戏', aliases=('ng', 'NGWordGame'), only_to_me=False)
async def NGWordGame(session: CommandSession):
    sender = copy(session.ctx['sender'])
    if session.is_first_run:
        FSM = NGFSM(session.ctx['group_id'])
        global firster
        firster = session.ctx['user_id']
        print(firster)
    else:
        #sender = copy(session.ctx['sender'])
        #print("sender:",sender)
        
        sender['isSU'] = await perm.check_permission(session.bot, session.ctx, perm.SUPERUSER)
        print(firster)
        if firster == session.ctx['user_id']:
            sender['isSt'] =True
        else:
            sender['isSt'] =False
        print("isSt:",sender['isSt'])
        
        #print("sender:",sender)
        FSM = session.state['FSM']
        #print("FSM:",FSM)
        FSM.RecieveInput(sender, session.current_arg_text)

    session.state['FSM'] = FSM
    #print("session:",str(session))
    ispause = await SessionReply(FSM, session)
    #print("ispause:",ispause)
    await SendPrivate(FSM, session)
    if ispause:
        session.pause()



async def SessionReply(FSM: NGFSM, session: CommandSession) -> bool:
    if not FSM.reply:
        return True
    else:
        for r in FSM.reply:
            await session.send(r.msg, at_sender=r.at_sender)
        return FSM.reply[-1].pause


async def SendPrivate(FSM: NGFSM, session: CommandSession):
    if FSM.private:
        bot = session.bot
        for p in FSM.private:
            await bot.send_private_msg(user_id=p.user_id, message=p.msg)


#@NGWordGame.args_parser
#async def _(session: CommandSession):
#    if session.is_first_run:
#        if not await perm.check_permission(session.bot, session.ctx, perm.SUPERUSER):
#            await session.send('请联系超级用户启动NG词语游戏')
#            session.finish()
