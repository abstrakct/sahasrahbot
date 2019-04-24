from ..util import orm

async def get_parameter(guild_id, parameter):
    result = await orm.select(
        'SELECT * from config WHERE guild_id=%s AND parameter=%s;',
        [guild_id, parameter]
    )
    return result[0]

async def get_parameters_by_guild(guild_id):
    result = await orm.select(
        'SELECT * from config WHERE guild_id=%s;',
        [guild_id]
    )
    return result

async def set_parameter(guild_id, parameter, value):
    await delete_parameter(guild_id, parameter)
    await orm.execute(
        'INSERT INTO config (`guild_id`,`parameter`,`value`) values (%s, %s, %s)',
        [guild_id,parameter,value]
    )

async def delete_parameter(guild_id, parameter):
    await orm.execute(
        'DELETE FROM config WHERE guild_id=%s AND parameter=%s',
        [guild_id,parameter]
    )