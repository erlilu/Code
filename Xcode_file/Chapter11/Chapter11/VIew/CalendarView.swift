//
//  CalendarView.swift
//  Chapter11
//
//  Created by Jethro Ming on 2026/7/4.
//


import SwiftUI

struct CalendarView: View {
    
    @State var viewModel = ViewModel()
    // 工作周数
    let daysInWeek = ["日","一","二","三","四","五","六"]
    // 网格参数
    let gridItemLayout = Array(repeating: GridItem(), count: 7)
    
    var body: some View {
        NavigationStack {
            VStack {
                //使用视图
                yearMonthView
                
                LazyVGrid(columns: gridItemLayout) {
                    weekView
                    firstDayOfWeekForMonthView
                    daysOfMonthView
                }
            }
            
        }
    }
    
    // 当前年月
    private var yearMonthView: some View {
        
        // 使用currentDate观察对象
        Text("\(viewModel.currentDate, formatter: DateFormatter.yearMonth)")
            .font(.largeTitle)
            .padding(.top, 16)
    }
    
    
    // 工作周
    private var weekView: some View {
        ForEach(daysInWeek, id: \.self) { day in
            Text(day)
                .font(.headline)
                .frame(maxWidth: .infinity)
        }
    }
    
    
    // 日历时间
    private var daysOfMonthView: some View {
        // 更换数据源
        ForEach(viewModel.daysOfMonth(), id:\.self) { day in
            Text("\(day.day)")
                .font(.system(size: 20))
                .frame(maxWidth: .infinity, minHeight: 48)
                .foregroundStyle(day.isSameDay(as: viewModel.selectedDate) ? Color.white : Color.black)
                .background(day.isSameDay(as: viewModel.selectedDate) ? Color.blue : Color.clear)
                .clipShape(ConcentricRectangle(corners: 8))
                // 单击事件
                .onTapGesture {
                    viewModel.selectedDate = day
                }
        }
    }
    
    
    // 日历起始日期
    private var firstDayOfWeekForMonthView: some View {
        ForEach(0 ..< viewModel.firstDayOfWeekForMonth(), id: \.self) { _ in
            Text(" ")
                .frame(maxWidth: .infinity, minHeight: 48)
        }
    }
    
}



#Preview {
    CalendarView()
}
