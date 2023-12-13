# [Game Programming Design Patterns](https://gameprogrammingpatterns.com/)

## Command
* Separate keyboard controls and command logic.
```cpp
class Command {
public:
  virtual ~Command() {}
  virtual void execute() = 0;
};
```

* Create a class that inherits from Command for each action.

```cpp
class InputHandler {
public:
  void handleInput();
  // Methods to bind commands...
private:
  Command* buttonX_;
  Command* buttonY_;
  Command* buttonA_;
  Command* buttonB_;
};
```

For a player actor, pass in a pointer to actor (player object) to Command execute.  
Call action from actor for specified action.