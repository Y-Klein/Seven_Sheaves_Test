from logik.stage_A import soldiers,beds,were_scheduled,waiting_list


def select(b = beds):
    A = []
    B = []
    room_ = []
    fool = []
    ampty = []
    half_full = []

    for bed in b:
        if bed.building_number == 1:
            A.append(bed)
        else:
            B.append(bed)

    for bed in range(80):
        for room in range(10):
            caunt = 0
            if A[bed].number_of_room == room +1:
                room_.append(A[bed])
            for beds in room_:
                if beds.soldier_number is not None:
                    caunt += 1
            if caunt == 8:
                fool.append(room +1)
            elif caunt < 8 and caunt > 0 :
                half_full.append(room +1)
            else:
                ampty.append(room +1)

    return {"fool":fool,"ampty":ampty}
