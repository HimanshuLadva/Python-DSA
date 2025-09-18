# https://leetcode.com/problems/design-task-manager?envType=daily-question&envId=2025-09-18
# 3408. Design Task Manager

# #pending - time limit exceed
# #MIMP
class TaskManager(object):
    def __init__(self, tasks):
        self.task_list = tasks
        self.task_map = {x[1]: x for x in tasks} 
        
    def display(self):
        for x in self.task_list:
            print(x)
        print('------------------------------')

    def add(self, userId,taskId,priority):
        self.task_list.append([userId,taskId,priority])
        self.task_map[taskId] = [userId,taskId,priority]
        

    def edit(self, taskId, newPriority):
        task = self.task_map[taskId]

        if task:
            updated_task = [task[0],task[1], newPriority]

            self.task_map[taskId] = updated_task
            
            for i,x in enumerate(self.task_list):
                if x[1] == taskId:
                    self.task_list[i] = updated_task
                    break    

    def rmv(self, taskId):
        task = self.task_map.pop(taskId,None)
        if task:
            self.task_list.remove(task) 

    def execTop(self):
        if not self.task_list:
            return -1

        top_task = None
        for task in self.task_list: 
            if (
                top_task is None
                or task[2] > top_task[2] 
                or (task[2] == top_task[2] and task[1] > top_task[1]) 
            ):
                top_task = task

        if top_task:
            self.task_list.remove(top_task)
            return top_task[0]
        return -1

        
    def execTopV2(self):
        if not self.task_list:
            return -1
        
        max_priority = max(x[2] for x in self.task_list)
        print(f"max_priority = {max_priority}")

        
        result = [x for x in self.task_list if x[2] == max_priority]
        print(f"result = {result}")
        
        if not result:
            return -1
        else:
            top_task = max(result, key=lambda x: x[1])
            self.task_list.remove(top_task)
            return top_task[0]
    
    def execTopV1(self):
        if not self.task_list:
            return -1
        max = 0
        for x in self.task_list:
            if x[2] > max:
                max = x[2]
        
        result = [x for x in self.task_list if x[2] == max]
        
        if len(result) == 0:
            return -1
        else:
            max = result[0][1]
            user_id = result[0][0]
            temp = result[0]
            for x in result:
                if x[1] > max:
                    max = x[1]
                    user_id = x[0]
                    temp = x
                    print(temp)
            
            if temp in self.task_list:
                self.task_list.remove(temp)
                return user_id
            else: 
                return -1
        
# task_list = [[1, 101, 10], [2, 102, 20], [3, 103, 15]]
# task_list = [[1, 101, 15], [2, 102, 20], [3, 103, 15]]
# obj = TaskManager(task_list)
# obj.add(4,104,5)
# obj.edit(102,8)
# obj.execTop()

task_list = [[3,0,49],[8,12,19]]
obj = TaskManager(task_list)
print(obj.execTop())
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
