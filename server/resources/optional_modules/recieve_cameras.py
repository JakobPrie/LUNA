PRIORITY = 7


# Dieses Modul empfängt alle Kamerabilder von allen Räumen und speichert sie im
# Local_storage unter folgendem Schema:
#Local_storage = {'LUNA_cams': {roomname1: {camname1: frame1, camname2: frame2}, roomname2:{camname3: frame3}}}

def start(luna, profile):
    profile['LUNA_cams'] = {}

def run(luna, profile):
    profile['LUNA_cams'] = {}
    for room in luna.rooms.copy().values():
        cams = room.Clientconnection.readanddelete('LUNA_room_cam_frames')
        # cams: [(frame, name), (frame, name),...]
        if cams is not None:
            profile['LUNA_cams'][room.name] = {}
            for frame, camname in cams:
                profile['LUNA_cams'][room.name][camname] = frame
