# cross_user_merge_engine.py
# Facilitates symbolic merging between two users' Fractality node structures

def merge_nodes(user_a_node, user_b_node):
    merged = {
        "id": f"merged_{user_a_node['id']}_{user_b_node['id']}",
        "label": f"{user_a_node['label']} ⊕ {user_b_node['label']}",
        "tags": list(set(user_a_node.get("tags", []) + user_b_node.get("tags", []))),
        "style": {
            "color": "#bdf",
            "glow": True,
            "blend": "convergent"
        },
        "source_users": [user_a_node["user"], user_b_node["user"]]
    }
    print(f"Merged node created: {merged['label']}")
    return merged

# Example
if __name__ == "__main__":
    node_a = {"id": "a1", "label": "Wonder", "tags": ["dream"], "user": "grazi"}
    node_b = {"id": "b1", "label": "Inquiry", "tags": ["focus"], "user": "gemini"}
    merge_nodes(node_a, node_b)
