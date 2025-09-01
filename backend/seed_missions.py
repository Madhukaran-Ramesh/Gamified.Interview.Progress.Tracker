from backend.missions import add_mission

# Example missions for initial setup
missions = [
    {
        'name': 'Array Basics',
        'description': 'Solve basic array manipulation problems.',
        'stage': 1,
        'level': 1,
        'skill_type': 'algorithms',
        'is_timed': False,
        'time_limit': 0,
        'hurdle': ''
    },
    {
        'name': 'Linked List Challenge',
        'description': 'Implement and reverse a linked list.',
        'stage': 1,
        'level': 2,
        'skill_type': 'data structures',
        'is_timed': True,
        'time_limit': 300,
        'hurdle': 'Reverse a linked list in 5 minutes.'
    },
    {
        'name': 'System Design Basics',
        'description': 'Design a URL shortener.',
        'stage': 2,
        'level': 1,
        'skill_type': 'system design',
        'is_timed': False,
        'time_limit': 0,
        'hurdle': ''
    }
]

def seed_missions():
    for m in missions:
        add_mission(**m)

if __name__ == "__main__":
    seed_missions()
    print("Missions seeded.")
