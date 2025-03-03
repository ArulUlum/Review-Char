import enka
import asyncio

FIGHT_PROPS_TO_SHOW = (
    enka.gi.FightPropType.FIGHT_PROP_MAX_HP,
    enka.gi.FightPropType.FIGHT_PROP_CUR_ATTACK,
    enka.gi.FightPropType.FIGHT_PROP_CUR_DEFENSE,
    enka.gi.FightPropType.FIGHT_PROP_ELEMENT_MASTERY,
    enka.gi.FightPropType.FIGHT_PROP_CRITICAL,
    enka.gi.FightPropType.FIGHT_PROP_CRITICAL_HURT,
    enka.gi.FightPropType.FIGHT_PROP_CHARGE_EFFICIENCY,
)

stat_name = {
    "Crit Rate": 20,
    "Crit Demage": 22,
    "Energy Recharge": 23,
    "Elemental Mastery": 28,
    "HP": 2000,
    "ATK": 2001,
    "DEF": 2002,
    "Demage Bonus": 45
}

def matching_name(key):
    matching_key = {v: k for k, v in stat_name.items()}
    name = matching_key.get(key, 'Unknown')
    return name

async def getGenshinInfo(UID):
    async with enka.GenshinClient(enka.gi.Language.ENGLISH) as client:
        # Update assets
        await client.update_assets()
        
        try:
            response = await client.fetch_showcase(UID)
            return response
        except enka.errors.PlayerDoesNotExistError:
            return "Akun Tidak Ditemukan."
        except enka.errors.GameMaintenanceError:
            return "Game sedang maintenance."
        except enka.errors.WrongUIDFormatError:
            return "Kesalahan Format UID"

#For Testing
# async def main():
#     async with enka.GenshinClient(enka.gi.Language.ENGLISH) as client:
#         # Update assets
#         await client.update_assets()

#         try:
#             response = await client.fetch_showcase(12321)
#         except enka.errors.PlayerDoesNotExistError:
#             return print("Player does not exist.")
#         except enka.errors.GameMaintenanceError:
#             return print("Game is in maintenance.")
#         except Exception as e:
#             return print(e)

#         print("Name:", response.player.nickname)
#         print("Level:", response.player.level)
#         print("Achievements:", response.player.achievements)
#         print("Namecard:", response.player.namecard.full)
#         print("Profile picture side icon:", response.player.profile_picture_icon.side)

#         for character in response.characters:
#             print("\n===============================\n")
#             print(
#                 f"Lv. {character.level}/{character.max_level} {character.name} (C{character.constellations_unlocked})"
#             )
#             print(f"Rarity: {character.rarity} ★")
#             print("Element:", character.element.name.title())
#             print("Side icon:", character.icon.side)
#             print(f"Talent levels: {'/'.join(str(talent.level) for talent in character.talents)}")
#             if character.namecard is not None:
#                 print("Namecard:", character.namecard.full)

#             if character.costume is not None:
#                 print("Costume side icon:", character.costume.icon.side)

#             weapon = character.weapon
#             print("\nWeapon:")
#             print(f"Lv. {weapon.level}/{weapon.max_level} {weapon.name} (R{weapon.refinement})")
#             print(f"Rarity: {weapon.rarity} ★")
#             for stat in weapon.stats:
#                 print(stat.name, stat.formatted_value)

#             print("\nStats:")
#             for stat_type, stat in character.stats.items():
#                 if stat_type in FIGHT_PROPS_TO_SHOW:
#                     print(matching_name(stat.type), stat.formatted_value)
#             dmg_bonus = character.highest_dmg_bonus_stat
#             print(matching_name(dmg_bonus.type), dmg_bonus.formatted_value)

#             print("\nArtifacts:")
#             for artifact in character.artifacts:
#                 main_stat = artifact.main_stat
#                 print(
#                     f"Lv. {artifact.level} {artifact.name}: {main_stat.name} {main_stat.formatted_value}"
#                 )
#                 for substat in artifact.sub_stats:
#                     print(f"- {substat.name} {substat.formatted_value}")
#                 print("")

# asyncio.run(main())