def route_action(current_scene: str, user_input: str) -> str:
    
    user_input = user_input.strip()

    if current_scene == "school_room":
        if user_input == "假装肚子疼":
            return "courtyard"
        elif user_input == "翻窗":
            return "library_detention"
        else:
            return "detention"

    elif current_scene == "courtyard":
        if user_input == "挖花盆":
            return "temple_fair"
        elif user_input == "翻墙":
            return "wall_climb"
        else:
            return "courtyard"  # 无效输入，留在原地

    elif current_scene == "wall_climb":
        if user_input == "向右":
            return "gate"
        elif user_input == "向左":
            return "temple_fair"
        else:
            return "wall_climb"  # 无效输入，留在原地

    else:
        return current_scene