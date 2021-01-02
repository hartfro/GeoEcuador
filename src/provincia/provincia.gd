extends Area2D

export(PackedScene) var Polygon


func _ready():
	if Polygon:
		remove_child($CollisionShape2D)
		add_child(Polygon.instance())


func _on_Provincia_input_event(viewport, event, shape_idx):
	if event is InputEventMouseButton and event.button_index == BUTTON_LEFT \
			&& event.pressed:
		print("Just pressed " + name)
